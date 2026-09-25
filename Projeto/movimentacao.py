import json
from pathlib import Path

from catalago import catalogo

_PASTA = Path("dados")
_FILE  = _PASTA / "movimentacoes.json"


def salvar_movimentacoes(movs):
    _PASTA.mkdir(exist_ok=True)
    with open(_FILE, "w", encoding="utf-8") as f:
        json.dump(movs, f, indent=2, ensure_ascii=False)


def carregar_movimentacoes():
    if _FILE.exists():
        with open(_FILE, encoding="utf-8") as f:
            return json.load(f)
    salvar_movimentacoes([])
    return []


def adicionar(movs, tipo, cod, qtd, valor_custo, valor_venda):
    movs.append({
        "tipo": tipo,
        "cod": cod,
        "nome": catalogo[cod]["nome"],
        "quantidade": qtd,
        "valor_custo": valor_custo,
        "valor_venda": valor_venda,
    })
    salvar_movimentacoes(movs)