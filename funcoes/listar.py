from sql.db import get_db
import mysql.connector

def listar_produtos():
    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = "SELECT * FROM produtos"
        cursor.execute(sql)

        produtos = cursor.fetchall()

        if produtos:
            print("--- Lista de Produtos ---")
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Descrição: {produto[2]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
        else:
            print("Nenhum produto encontrado.")

    except mysql.connector.Error as err:
        print(f"❌ Erro ao listar produtos: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()