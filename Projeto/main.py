import os #limpar tela
from tela_inicial import mostrar_tela_inicial #tela inicial
from rich.console import Console #exibir mensagens formatadas
from rich.table import Table #exibir tabelas formatadas
from rich.panel import Panel #exibir painéis formatados
from rich import box #estilos de borda para tabelas e painéis 
from catalago import catalogo #catálogo de produtos
import estoque as estoque_db #funções para manipular o estoque (carregar, salvar, registrar entradas/saídas)
import movimentacao as mov_db #funções para manipular as movimentações (carregar, salvar, adicionar nova movimentação)

def limpar_tela(): #limpa a tela do terminal (funciona no Windows)
    os.system("cls") #comando para limpar a tela no Windows

console = Console() #instância do console para exibir mensagens formatadas


def exibir_catalogo(dados_estoque):
    tabela = Table(title="Catálogo de Produtos", box=box.SIMPLE_HEAVY)
    tabela.add_column("Cód.", style="blue", justify="right")
    tabela.add_column("Nome", style="white")
    tabela.add_column("Setor", style="yellow")
    tabela.add_column("Estoque", justify="right", style="green")
    tabela.add_column("Custo (R$)", justify="right")
    tabela.add_column("Venda (R$)", justify="right")

    for cod, prod in catalogo.items():
        est = dados_estoque[cod]
        tabela.add_row(
            cod, prod["nome"], prod["setor"],
            str(est["quantidade"]),
            f"{est['custo_medio']:.2f}",
            f"{est['preco_venda']:.2f}",
        )
    console.print(tabela)


def tela_entrada(dados_estoque, movimentacoes):
    console.print("\n[bold cyan]--- REGISTRO DE ENTRADA ---[/bold cyan]")
    exibir_catalogo(dados_estoque)

    cod = console.input("\nCódigo do produto: ").strip()
    if cod not in catalogo:
        console.print("[red]Código inválido.[/red]")
        return
    try:
        quantidade  = int(console.input("Quantidade: ").strip())
        custo_unit  = float(console.input("Valor de custo unitário (R$): ").strip())
        preco_venda = float(console.input("Valor de venda unitário (R$): ").strip())
    except ValueError:
        console.print("[red]Valores inválidos.[/red]")
        return

    estoque_db.registrar_entradas(dados_estoque, cod, quantidade, custo_unit, preco_venda)
    mov_db.adicionar(movimentacoes, "ENTRADA", cod, quantidade, custo_unit, preco_venda)
    console.print(f"[green]Entrada registrada: {quantidade}x {catalogo[cod]['nome']}[/green]")


def tela_saida(dados_estoque, movimentacoes):
    console.print("\n[bold yellow]--- REGISTRO DE SAÍDA ---[/bold yellow]")
    exibir_catalogo(dados_estoque)

    cod = console.input("\nCódigo do produto: ").strip()
    if cod not in catalogo:
        console.print("[red]Código inválido.[/red]")
        return
    try:
        quantidade = int(console.input("Quantidade: ").strip())
    except ValueError:
        console.print("[red]Valor inválido.[/red]")
        return

    try:
        item = dados_estoque[cod]
        mov_db.adicionar(movimentacoes, "SAÍDA", cod, quantidade, item["custo_medio"], item["preco_venda"])
        estoque_db.registrar_saidas(dados_estoque, cod, quantidade)
        console.print(f"[yellow]Saída registrada: {quantidade}x {catalogo[cod]['nome']}[/yellow]")
    except ValueError as e:
        console.print(f"[red]{e}[/red]")


def gerar_relatorio(dados_estoque, movimentacoes):
    console.print("\n")
    console.print(Panel("[bold white]RELATÓRIO DE ESTOQUE[/bold white]", style="blue"))

    tabela_est = Table(title="Posição Atual do Estoque", box=box.SIMPLE_HEAVY)
    tabela_est.add_column("Cód.", style="blue", justify="right")
    tabela_est.add_column("Produto", style="white")
    tabela_est.add_column("Setor", style="yellow")
    tabela_est.add_column("Qtd.", justify="right")
    tabela_est.add_column("Custo Médio", justify="right")
    tabela_est.add_column("Venda", justify="right")
    tabela_est.add_column("Valor em Estoque", justify="right", style="green")

    total_em_estoque = 0.0
    for cod, prod in catalogo.items():
        item = dados_estoque[cod]
        valor = item["quantidade"] * item["custo_medio"]
        total_em_estoque += valor
        tabela_est.add_row(
            cod, prod["nome"], prod["setor"],
            str(item["quantidade"]),
            f"R$ {item['custo_medio']:.2f}",
            f"R$ {item['preco_venda']:.2f}",
            f"R$ {valor:.2f}",
        )

    console.print(tabela_est)
    console.print(f"  [bold]Total em estoque (custo):[/bold]  [green]R$ {total_em_estoque:.2f}[/green]\n")

    if not movimentacoes:
        console.print("[dim]Nenhuma movimentação registrada.[/dim]")
        return

    tabela_mov = Table(title="Histórico de Movimentações", box=box.SIMPLE_HEAVY)
    tabela_mov.add_column("#", justify="right", style="dim")
    tabela_mov.add_column("Tipo", justify="center")
    tabela_mov.add_column("Cód.", justify="right", style="cyan")
    tabela_mov.add_column("Produto")
    tabela_mov.add_column("Qtd.", justify="right")
    tabela_mov.add_column("Custo Unit.", justify="right")
    tabela_mov.add_column("Venda Unit.", justify="right")
    tabela_mov.add_column("Total Custo", justify="right")
    tabela_mov.add_column("Total Venda", justify="right")

    total_entradas = total_saidas = 0
    receita = custo_saidas = 0.0

    for i, m in enumerate(movimentacoes, 1):
        cor = "green" if m["tipo"] == "ENTRADA" else "yellow"
        t_custo = m["quantidade"] * m["valor_custo"]
        t_venda  = m["quantidade"] * m["valor_venda"]

        tabela_mov.add_row(
            str(i), f"[{cor}]{m['tipo']}[/{cor}]",
            m["cod"], m["nome"], str(m["quantidade"]),
            f"R$ {m['valor_custo']:.2f}", f"R$ {m['valor_venda']:.2f}",
            f"R$ {t_custo:.2f}", f"R$ {t_venda:.2f}",
        )

        if m["tipo"] == "ENTRADA":
            total_entradas += m["quantidade"]
        else:
            total_saidas += m["quantidade"]
            receita      += t_venda
            custo_saidas += t_custo

    console.print(tabela_mov)
    console.print(f"  [bold]Total de itens entrados:[/bold]  {total_entradas}")
    console.print(f"  [bold]Total de itens saídos: [/bold]  {total_saidas}")
    console.print(f"  [bold]Receita das saídas:    [/bold]  [green]R$ {receita:.2f}[/green]")
    console.print(f"  [bold]Custo das saídas:      [/bold]  [red]R$ {custo_saidas:.2f}[/red]")
    console.print(f"  [bold]Lucro realizado:       [/bold]  [magenta]R$ {receita - custo_saidas:.2f}[/magenta]\n")

def voltar_tela_inicial():
    limpar_tela()
    mostrar_tela_inicial()
    input()
    limpar_tela()

def menu():
    dados_estoque = estoque_db.carregar_estoque()
    movimentacoes = mov_db.carregar_movimentacoes()

    opcoes = {
        "1": lambda: tela_entrada(dados_estoque, movimentacoes),
        "2": lambda: tela_saida(dados_estoque, movimentacoes),
        "3": lambda: exibir_catalogo(dados_estoque),
        "4": lambda: gerar_relatorio(dados_estoque, movimentacoes),
        "5": lambda: voltar_tela_inicial(),
    }

    while True:
        console.print(Panel(
            "[1] Registrar Entrada\n"
            "[2] Registrar Saída\n"
            "[3] Ver Estoque\n"
            "[4] Gerar Relatório\n"
            "[5] Tela Inicial\n"
            "[0] Sair",
            title="[bold]Controle de Estoque[/bold]",
            style="blue",
        ))

        opcao = console.input("Opção: ").strip()

        if opcao == "0":
            console.print("[bold]Encerrando...[/bold]")
            break

        handler = opcoes.get(opcao)
        if handler:
            handler()
        else:
            console.print("[red]Opção inválida.[/red]")

if __name__ == "__main__":
    limpar_tela()
    mostrar_tela_inicial()

    input()

    limpar_tela()
    menu()
