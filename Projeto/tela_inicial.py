from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

console = Console()

def mostrar_tela_inicial():
    titulo = Text("📦 SISTEMA DE ESTOQUE", style="bold cyan")

    lista = Text()
    lista.append("✔ Cadastro de produtos\n", style="white")
    lista.append("✔ Entrada e saída de estoque\n", style="white")
    lista.append("✔ Relatórios\n\n", style="white")
    lista.append("Pressione ENTER para continuar...", style="bold green")

    conteudo = Align.center(
        Text.assemble(
            "\n",
            titulo,
            "\n\n",
            lista,
            "\n"
        ),
        vertical="middle"
    )

    painel = Panel(
        conteudo,
        box=box.DOUBLE,
        border_style="cyan",
        padding=(1, 4),
        title="🚀 Bem-vindo",
        title_align="center"
    )

    console.clear()
    console.print(painel)

mostrar_tela_inicial()