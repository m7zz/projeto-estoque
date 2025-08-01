from sql.db import get_db
import mysql.connector
from datetime import date

def registrar_venda(id_produto: int, quantidade: int):
    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = """SELECT quantidade FROM produtos WHERE id = %s;"""
        cursor.execute(sql, (id_produto,)) 
        resultado = cursor.fetchone()

        if resultado is None:
            print('⚠️ Produto não encontrado.')
            return  

        estoque_atual = resultado[0]

       
        if estoque_atual < quantidade:
            print('⚠️ Sem estoque suficiente.')
            return 

       
        data_hoje = date.today()
        sql = """
            INSERT INTO vendas (id_produto, quantidade, data_feita)
            VALUES (%s, %s, %s);
        """  
        cursor.execute(sql, (id_produto, quantidade, data_hoje))

      
        sql = "UPDATE produtos SET quantidade = quantidade - %s WHERE id = %s;"
        cursor.execute(sql, (quantidade, id_produto))

        
        conn.commit()
        print('✅ Venda registrada com sucesso.')

    except mysql.connector.Error as err:
        print(f"❌ Erro ao registrar venda: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
