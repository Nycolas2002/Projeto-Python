# 📦 Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em **Python**, com o objetivo de praticar conceitos de programação, organização de código em módulos, manipulação de arquivos JSON e gerenciamento de entradas e saídas de produtos.

O projeto simula um sistema simples de estoque, permitindo cadastrar produtos, controlar quantidades e registrar movimentações.

## 🎯 Objetivo

O projeto foi desenvolvido como forma de aprendizado e prática de programação em Python, trabalhando principalmente com:

* Variáveis e tipos de dados
* Funções
* Condicionais
* Estruturas de repetição
* Dicionários e listas
* Tratamento de exceções
* Organização do código em módulos
* Leitura e escrita de arquivos JSON
* Controle de estoque
* Registro de movimentações

## ⚙️ Funcionalidades

O sistema possui funcionalidades para:

* 🏠 Exibir uma tela inicial
* 📦 Visualizar o estoque
* ➕ Registrar entrada de produtos
* ➖ Registrar saída de produtos
* 📋 Consultar informações dos produtos
* 📊 Gerar relatório de movimentações
* 💾 Salvar os dados automaticamente em arquivos JSON

### Categorias de produtos

O sistema trabalha com categorias como:

* 🥖 Padaria
* 🥤 Bebidas
* 🍽️ Rotisseria

## 🗂️ Estrutura do projeto

```text
Projeto/
│
├── main.py
├── catalago.py
├── estoque.py
├── movimentacao.py
├── tela_inicial.py
│
├── dados/
│   ├── estoque.json
│   └── movimentacoes.json
│
└── README.md
```

### 📄 Descrição dos arquivos

| Arquivo              | Descrição                                            |
| -------------------- | ---------------------------------------------------- |
| `main.py`            | Arquivo principal responsável por executar o sistema |
| `catalago.py`        | Gerenciamento do catálogo de produtos                |
| `estoque.py`         | Controle das quantidades disponíveis no estoque      |
| `movimentacao.py`    | Registro das entradas e saídas                       |
| `tela_inicial.py`    | Exibição e organização da tela inicial               |
| `estoque.json`       | Armazena os dados atuais do estoque                  |
| `movimentacoes.json` | Armazena o histórico de movimentações                |

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **JSON**
* Terminal/Console

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd Projeto
```

### 3. Execute o programa

```bash
python main.py
```

> Dependendo da configuração do seu computador, pode ser necessário utilizar `python3 main.py`.

## 💾 Armazenamento dos dados

Os dados do sistema são armazenados localmente em arquivos **JSON**.

O arquivo:

```text
dados/estoque.json
```

é utilizado para armazenar as informações relacionadas aos produtos e suas quantidades.

Já:

```text
dados/movimentacoes.json
```

mantém o histórico das movimentações realizadas no sistema.

## 📚 O que aprendi com este projeto

Durante o desenvolvimento deste projeto, pude praticar conceitos importantes da programação em Python, principalmente a criação de funções, utilização de estruturas de decisão e repetição, manipulação de arquivos e organização de um projeto em diferentes módulos.

Também foi uma oportunidade para entender melhor como diferentes partes de um programa podem trabalhar juntas e como os dados podem ser persistidos utilizando arquivos JSON.

## 🔮 Melhorias futuras

Algumas funcionalidades que podem ser adicionadas futuramente:

* [ ] Interface gráfica
* [ ] Banco de dados MySQL
* [ ] Sistema de login e usuários
* [ ] Pesquisa de produtos
* [ ] Alertas de estoque baixo
* [ ] Relatórios mais completos
* [ ] Exportação de relatórios
* [ ] Dashboard com gráficos
* [ ] Integração com banco de dados

## 👨‍💻 Autor

**Nycolas Robert Batista Ramos**

Estudante de **Análise e Desenvolvimento de Sistemas**, com interesse nas áreas de **Dados, Banco de Dados, Engenharia de Dados, Arquitetura de Dados e Business Intelligence (BI)**.

### Tecnologias e conhecimentos

* Python
* SQL
* MySQL
* Engenharia de Prompt

---

⭐ Este projeto foi desenvolvido para fins de estudo e prática de programação.
