"""Recolha reproduzível do indicador histórico de inscritos nos CSP."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

DATASET = "utentes-inscritos-em-cuidados-de-saude-primarios"
URL_BASE = (
    f"https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets/{DATASET}"
)


def recolher_historico(pasta_input):
    """Guarda o CSV e os metadados originais; reutiliza uma recolha existente."""
    pasta_input = Path(pasta_input)
    pasta_input.mkdir(parents=True, exist_ok=True)
    ficheiro_csv = pasta_input / "utentes_csp_historico_bruto.csv"
    ficheiro_api = pasta_input / "utentes_csp_metadados_api.json"
    ficheiro_recolha = pasta_input / "utentes_csp_recolha.json"
    ficheiros = [ficheiro_csv, ficheiro_api, ficheiro_recolha]

    parametros = {"order_by": "periodo ASC, ars ASC, aces ASC"}
    url_csv = f"{URL_BASE}/exports/csv?{urlencode(parametros)}"

    if any(f.exists() for f in ficheiros):
        if not all(f.exists() for f in ficheiros):
            raise ValueError(
                "A recolha está incompleta. Confirmar os três ficheiros em data/input."
            )
        recolha = json.loads(ficheiro_recolha.read_text(encoding="utf-8"))
        metadados_api = json.loads(ficheiro_api.read_text(encoding="utf-8"))
        if recolha.get("url_csv") != url_csv:
            raise ValueError(
                "A recolha guardada usa outros parâmetros. Preservar os ficheiros e usar outra pasta."
            )
        for ficheiro, campo in [
            (ficheiro_csv, "sha256_csv"),
            (ficheiro_api, "sha256_metadados"),
        ]:
            if hashlib.sha256(ficheiro.read_bytes()).hexdigest() != recolha[campo]:
                raise ValueError(f"O ficheiro bruto foi alterado: {ficheiro.name}.")
        return ficheiro_csv, metadados_api, recolha

    with urlopen(URL_BASE, timeout=60) as resposta:
        bytes_api = resposta.read()
        metadados_api = json.loads(bytes_api.decode("utf-8"))
        estado_api = resposta.status

    with urlopen(url_csv, timeout=90) as resposta:
        bytes_csv = resposta.read()
        estado_csv = resposta.status
        tipo_conteudo = resposta.headers.get("Content-Type", "")

    if not bytes_csv.decode("utf-8-sig").startswith("periodo;"):
        raise ValueError("A resposta não é o CSV esperado. Verificar o esquema da API.")

    recolha = {
        "dataset": DATASET,
        "url_metadados": URL_BASE,
        "url_csv": url_csv,
        "parametros": parametros,
        "recolhido_em_utc": datetime.now(timezone.utc).isoformat(),
        "estado_http_metadados": estado_api,
        "estado_http_csv": estado_csv,
        "content_type": tipo_conteudo,
        "metodo": "API oficial - exportação do histórico completo sem filtro temporal",
        "sha256_csv": hashlib.sha256(bytes_csv).hexdigest(),
        "sha256_metadados": hashlib.sha256(bytes_api).hexdigest(),
        "bytes_csv": len(bytes_csv),
    }

    ficheiro_csv.write_bytes(bytes_csv)
    ficheiro_api.write_bytes(bytes_api)
    ficheiro_recolha.write_text(
        json.dumps(recolha, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return ficheiro_csv, metadados_api, recolha
