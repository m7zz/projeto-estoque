from sql.db import get_db
import mysql.connector

def atualizar(id_produto: int,quantidade_nova: int):
    try:
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM produtos WHERE id = %s", (id_produto,))
        resultado = cursor.fetchone()

        if not resultado:
            return False  # Produto não encontrado

        cursor.execute(
            "UPDATE produtos SET quantidade = %s WHERE id = %s",
            (quantidade_nova, id_produto)
        )
        conn.commit()
        print('Atualização feita com exito.') #utilizei exito pois acho bonito

    except mysql.connector.Error as err:
        print(f"❌ Erro ao executa: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
