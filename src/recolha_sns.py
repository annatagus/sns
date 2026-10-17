"""Recolha reproduzível do indicador histórico de inscritos nos CSP (SNS).

A função :func:`recolher_historico` faz uma de duas coisas:

* se a pasta de entrada já tiver uma recolha completa, confirma que os bytes
  não mudaram (SHA-256) e devolve-a, sem voltar à API;
* se a pasta estiver vazia, descarrega o CSV e os metadados pela API oficial do
  Portal da Transparência e guarda os bytes originais e o registo da recolha.

Os ficheiros brutos nunca são substituídos. Para uma recolha nova, usar outra
pasta e conservar a anterior.
"""

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
PARAMETROS_CSV = {"order_by": "periodo ASC, ars ASC, aces ASC"}
URL_CSV = f"{URL_BASE}/exports/csv?{urlencode(PARAMETROS_CSV)}"

NOME_CSV = "utentes_csp_historico_bruto.csv"
NOME_METADADOS = "utentes_csp_metadados_api.json"
NOME_RECOLHA = "utentes_csp_recolha.json"

TIMEOUT_METADADOS_S = 60
TIMEOUT_CSV_S = 90


def _sha256(dados: bytes) -> str:
    return hashlib.sha256(dados).hexdigest()


def _verificar_assinatura(ficheiro: Path, esperado: str) -> None:
    """Para a execução se o ficheiro não tiver os mesmos bytes da recolha."""
    conteudo = ficheiro.read_bytes()
    if _sha256(conteudo) == esperado:
        return
    # Causa mais comum: o Git converteu os finais de linha (CRLF <-> LF) no
    # checkout. O conteúdo é o mesmo, mas os bytes e a assinatura mudam.
    so_finais_de_linha = esperado in {
        _sha256(conteudo.replace(b"\r\n", b"\n")),
        _sha256(conteudo.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")),
    }
    dica = (
        " Apenas os finais de linha diferem: confirmar o .gitattributes do "
        "repositório e voltar a fazer checkout dos ficheiros de data/."
        if so_finais_de_linha
        else ""
    )
    raise ValueError(f"O ficheiro bruto foi alterado: {ficheiro.name}.{dica}")


def recolher_historico(pasta_input):
    """Devolve ``(ficheiro_csv, metadados_api, recolha)``.

    Reutiliza uma recolha existente em ``pasta_input`` depois de verificar as
    assinaturas; caso contrário, faz uma recolha nova pela API oficial.
    """
    pasta_input = Path(pasta_input)
    pasta_input.mkdir(parents=True, exist_ok=True)
    ficheiro_csv = pasta_input / NOME_CSV
    ficheiro_api = pasta_input / NOME_METADADOS
    ficheiro_recolha = pasta_input / NOME_RECOLHA
    ficheiros = [ficheiro_csv, ficheiro_api, ficheiro_recolha]

    existentes = [f.exists() for f in ficheiros]
    if any(existentes):
        if not all(existentes):
            raise ValueError(
                "A recolha está incompleta. Confirmar os três ficheiros em "
                f"{pasta_input}: {', '.join(f.name for f in ficheiros)}."
            )
        recolha = json.loads(ficheiro_recolha.read_text(encoding="utf-8"))
        if recolha.get("url_csv") != URL_CSV:
            raise ValueError(
                "A recolha guardada usa outros parâmetros. Preservar os ficheiros "
                "e usar outra pasta."
            )
        _verificar_assinatura(ficheiro_csv, recolha["sha256_csv"])
        _verificar_assinatura(ficheiro_api, recolha["sha256_metadados"])
        metadados_api = json.loads(ficheiro_api.read_text(encoding="utf-8"))
        return ficheiro_csv, metadados_api, recolha

    with urlopen(URL_BASE, timeout=TIMEOUT_METADADOS_S) as resposta:
        bytes_api = resposta.read()
        estado_api = resposta.status
    metadados_api = json.loads(bytes_api.decode("utf-8"))

    with urlopen(URL_CSV, timeout=TIMEOUT_CSV_S) as resposta:
        bytes_csv = resposta.read()
        estado_csv = resposta.status
        tipo_conteudo = resposta.headers.get("Content-Type", "")

    if not bytes_csv.decode("utf-8-sig").startswith("periodo;"):
        raise ValueError("A resposta não é o CSV esperado. Verificar o esquema da API.")

    recolha = {
        "dataset": DATASET,
        "url_metadados": URL_BASE,
        "url_csv": URL_CSV,
        "parametros": PARAMETROS_CSV,
        "recolhido_em_utc": datetime.now(timezone.utc).isoformat(),
        "estado_http_metadados": estado_api,
        "estado_http_csv": estado_csv,
        "content_type": tipo_conteudo,
        "metodo": "API oficial - exportação do histórico completo sem filtro temporal",
        "sha256_csv": _sha256(bytes_csv),
        "sha256_metadados": _sha256(bytes_api),
        "bytes_csv": len(bytes_csv),
    }

    ficheiro_csv.write_bytes(bytes_csv)
    ficheiro_api.write_bytes(bytes_api)
    ficheiro_recolha.write_text(
        json.dumps(recolha, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return ficheiro_csv, metadados_api, recolha
