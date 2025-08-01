from sql.db import get_db
import mysql.connector

def remover_produto(id_produto: int):
    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = "DELETE FROM produtos WHERE id = %s;"
        cursor.execute(sql, (id_produto,))
        conn.commit()

        if cursor.rowcount > 0:
            print('✅ produto deletado com sucesso')
        else:
            print('⚠️ id nao encontrado')

    except mysql.connector.Error as err:
        print(f"❌ Erro ao deletar produto: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
