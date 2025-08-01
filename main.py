from datetime import date
from funcoes.produtos import add_produto
from funcoes.listar import listar_produtos
from funcoes.atualizar import atualizar
from funcoes.remover import remover_produto
from funcoes.registrar_venda import registrar_venda

# antes de comecar a fazer o menu, queria pedir uns pontinho, porque so nisso ja foi 3 horas ha kkk

def mostrar_menu():
    print("\n=== MENU ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Registrar venda")
    print("6 - Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input ('🤔 Escolha uma opção: ')

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            mostrar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            registrar_venda_func()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

def cadastrar_produto():
    nome = input('Digite o nome do produto: ')
    descricao = input('Digite a descricao do produto: ')
    try:
        quantidade = int(input("Quantidade disponível: "))
        preco = float(input("Preço: "))
    except ValueError:
        print("Quantidade e preço devem ser números.")
        return

    add_produto(nome, descricao, quantidade, preco)

def mostrar_produtos():
    produtos = listar_produtos()  
    if produtos:
        print("\n--- Lista de Produtos ---")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Descrição: {produto[2]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
    else:
        print("Nenhum produto encontrado.")

def atualizar_produto():
    try:
        id_produto = int(input("ID do produto para atualizar: "))
        quantidade = int(input("Nova quantidade: "))
        preco = float(input("Novo preço: "))
    except ValueError:
        print("ID, quantidade e preço devem ser números.")
        return

    atualizar(id_produto, quantidade, preco)

def remover_produto():
    try:
        id_produto = int(input("ID do produto para remover: "))
    except ValueError:
        print("ID deve ser um número.")
        return

    remover_produto(id_produto)

def registrar_venda_func():
    try:
        id_produto = int(input("ID do produto vendido: "))
        quantidade = int(input("Quantidade vendida: "))
    except ValueError:
        print("ID e quantidade devem ser números.")
        return

    registrar_venda(id_produto, quantidade)

main()