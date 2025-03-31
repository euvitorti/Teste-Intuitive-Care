import psycopg2
from psycopg2.extras import RealDictCursor
from banco_de_dados.database.conectar_bd import conectar_banco_de_dados
import os

# Obtém o diretório base do arquivo atual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho do arquivo SQL
SQL_BUSCAR_OPERADORAS = os.path.join(BASE_DIR, "..", "sql", "buscar_operadoras.sql")

def carregar_query(caminho_sql: str) -> str:
    """
    Carrega e retorna o conteúdo de um arquivo SQL.

    :param caminho_sql: Caminho para o arquivo SQL.
    :return: String contendo a query SQL.
    :raises Exception: Se o arquivo não for encontrado.
    """
    
    try:
        with open(caminho_sql, "r", encoding="utf8") as file:
            return file.read()
    except FileNotFoundError:
        raise Exception("Arquivo SQL não encontrado.")


def buscar_operadoras(termo: str):
    """
    Busca operadoras de saúde pela razão social no banco de dados.

    :param termo: Termo de busca para filtrar as operadoras.
    :return: Lista de operadoras encontradas ou None se não houver resultados.
    :raises Exception: Se houver erro ao conectar ou executar a consulta.
    """

    try:
        # Conecta ao banco de dados
        conn = conectar_banco_de_dados()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Carrega a query SQL do arquivo
        query = carregar_query(SQL_BUSCAR_OPERADORAS)

        # Executa a consulta com o termo de busca, prevenindo SQL Injection
        cursor.execute(query, (f"%{termo}%",))
        resultados = cursor.fetchall()

        # Retorna os resultados ou None se a lista estiver vazia
        return resultados if resultados else None

    except psycopg2.Error as e:
        raise Exception(f"Erro ao buscar operadoras: {str(e)}")

    finally:
        # Fecha o cursor e a conexão apenas se estiverem abertos
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
