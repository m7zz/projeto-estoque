# Sistema de Gerenciamento de Estoque

Este projeto é um sistema simples para gerenciar produtos e vendas em uma loja, desenvolvido em Python com conexão a um banco de dados MySQL.

## Funcionalidades

- Cadastrar novos produtos (nome, descrição, quantidade, preço)
- Listar produtos cadastrados
- Atualizar quantidade e preço dos produtos
- Remover produtos
- Registrar vendas com controle de estoque
- Listar vendas registradas

## Tecnologias usadas

- Python 3.x
- MySQL
- Biblioteca mysql-connector-python

## Como rodar o projeto

### Pré-requisitos

- Python 3 instalado
- MySQL instalado e configurado
- Criar um banco de dados e importar as tabelas `produtos` e `vendas`

### Passos para rodar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure seu banco de dados em sql/db.py (dados de conexão).

Execute o programa principal:

bash
Copiar
Editar
python main.py
Estrutura do projeto
bash
Copiar
Editar
├── acoes/               # Funções para operações no banco
├── sql/                 # Configuração do banco de dados e scripts SQL
├── main.py              # Script principal com o menu interativo
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
