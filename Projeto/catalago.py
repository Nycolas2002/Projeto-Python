class Produto:
    def __init__(self, nome, setor):
        self.nome  = nome
        self.setor = setor
 
 
class Padaria(Produto):
    def __init__(self, nome):
        super().__init__(nome, setor="Padaria")
 
 
class Bebidas(Produto):
    def __init__(self, nome):
        super().__init__(nome, setor="Bebidas")
 
 
class Rotisseria(Produto):
    def __init__(self, nome):
        super().__init__(nome, setor="Rotisseria")
 
 
produtos = [
    Padaria("Pão"),
    Bebidas("Leite"),
    Rotisseria("Mortadela"),
    Rotisseria("Presunto"),
    Rotisseria("Queijo"),
    Bebidas("Refrigerante"),
    Bebidas("Suco"),
    Bebidas("Água"),
    Padaria("Manteiga"),
    Padaria("Maionese"),
]
 
catalogo = {str(i): {"nome": p.nome, "setor": p.setor} for i, p in enumerate(produtos, 1)}