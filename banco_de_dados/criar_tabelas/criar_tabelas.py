import psycopg2
from database.conectar_bd import conectar_banco_de_dados

def criar_tabelas(sql_file_path):
    """
    Lê o script SQL e executa os comandos para criar as tabelas no banco de dados.

    Parâmetros:
    sql_file_path: Caminho do arquivo SQL contendo os comandos de criação de tabelas.
    """
    
    try:
        # Estabelece conexão com o banco de dados utilizando a função centralizada
        conn = conectar_banco_de_dados()
        cursor = conn.cursor()

        # Lê o conteúdo do arquivo SQL
        with open(sql_file_path, "r", encoding="utf8") as file:
            sql_script = file.read()

        # Executa o script SQL para criar as tabelas
        cursor.execute(sql_script)

        # Confirma as alterações no banco de dados
        conn.commit()
        print("Tabelas criadas com sucesso!")

    except psycopg2.Error as e:
        # Captura erros de banco de dados e exibe uma mensagem
        print(f"Erro ao criar tabelas: {e}")

    finally:
        # Garante que o cursor e a conexão sejam fechados, evitando vazamento de recursos
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            