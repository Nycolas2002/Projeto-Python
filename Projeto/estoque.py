import json
from pathlib import Path

_PASTA = Path("dados")
_FILE  = _PASTA / "estoque.json"

_ESTOQUE_INICIAL = {
    "1":  {"quantidade": 50, "custo_medio": 0.75,  "preco_venda": 1.50},
    "2":  {"quantidade": 30, "custo_medio": 4.20,  "preco_venda": 6.99},
    "3":  {"quantidade": 20, "custo_medio": 8.00,  "preco_venda": 14.90},
    "4":  {"quantidade": 20, "custo_medio": 9.50,  "preco_venda": 16.90},
    "5":  {"quantidade": 15, "custo_medio": 12.00, "preco_venda": 22.90},
    "6":  {"quantidade": 40, "custo_medio": 3.50,  "preco_venda": 6.50},
    "7":  {"quantidade": 25, "custo_medio": 5.00,  "preco_venda": 8.90},
    "8":  {"quantidade": 60, "custo_medio": 1.00,  "preco_venda": 2.50},
    "9":  {"quantidade": 30, "custo_medio": 6.00,  "preco_venda": 10.90},
    "10": {"quantidade": 20, "custo_medio": 5.50,  "preco_venda": 9.90},
}

def salvar_estoque(estoque):
    _PASTA.mkdir(exist_ok=True)
    with open(_FILE, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=2, ensure_ascii=False)

def carregar_estoque():
    if _FILE.exists():
        with open(_FILE, encoding="utf-8") as f:
            return json.load(f)
    salvar_estoque(_ESTOQUE_INICIAL)
    return _ESTOQUE_INICIAL.copy()

def registrar_entradas(estoque, cod, quantidade, valor_custo, valor_venda):
    item = estoque[cod]
    total_qtd = item["quantidade"] + quantidade
    item["custo_medio"] = (item["custo_medio"] * item["quantidade"] + valor_custo * quantidade) / total_qtd
    item["quantidade"]  = total_qtd
    item["preco_venda"] = valor_venda
    salvar_estoque(estoque)

def registrar_saidas(estoque, cod, quantidade):
    if estoque[cod]["quantidade"] < quantidade:
        raise ValueError("Estoque insuficiente.")
    estoque[cod]["quantidade"] -= quantidade
    salvar_estoque(estoque)

