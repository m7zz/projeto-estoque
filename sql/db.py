import mysql.connector

def get_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='B4l90MiNe',
        database='estoque'
    )

if __name__ == '__main__':
    try:
        conn = get_db()
        print('Conexão com sucesso')
        cursor = conn.cursor()

        with open('./sql/dump.sql', 'r', encoding='utf-8') as file:
            sql = file.read()

        # Divide os comandos SQL por ponto e vírgula
        comandos = sql.split(';')

        for comando in comandos:
            comando = comando.strip()
            if comando:  # ignora comandos vazios
                cursor.execute(comando)

        conn.commit()
        print('O dump foi executado com sucesso')

    except mysql.connector.Error as err:
        print(f'Erro ao executar dump: {err}')
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals() and conn.is_connected(): conn.close()
