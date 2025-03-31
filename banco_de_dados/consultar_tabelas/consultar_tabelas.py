import os
import psycopg2
from database.conectar_bd import conectar_banco_de_dados

# Diretório base para localizar o arquivo SQL
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
arquivo_query = os.path.join(BASE_DIR, "..", "sql", "consultar_operadoras.sql")

def consultar_top_operadoras(data_inicio, data_fim):
    """
    Executa a query SQL para consultar as top operadoras com base em um intervalo de datas.
    
    Parâmetros:
        data_inicio: Data de início no formato 'YYYY-MM-DD'.
        data_fim: Data de fim no formato 'YYYY-MM-DD'.
    
    Retorna:
        tuple: Uma tupla contendo a lista de colunas e os resultados da consulta.
    """
    try:
        # Conecta ao banco de dados utilizando a função centralizada
        conn = conectar_banco_de_dados()
        cursor = conn.cursor()
        
        # Abre e lê o arquivo SQL contendo a query.
        with open(arquivo_query, 'r', encoding='utf8') as f:
            query = f.read()
        
        # Executa a query com os parâmetros, evitando injeção de SQL.
        cursor.execute(query, {'data_inicio': data_inicio, 'data_fim': data_fim})
        
        # Extrai os nomes das colunas da consulta a partir da descrição do cursor
        colunas = [desc[0] for desc in cursor.description]
        
        # Recupera todos os resultados da query
        resultados = cursor.fetchall()
        
        return colunas, resultados
    except psycopg2.Error as e:
        print(f"Erro ao executar consulta: {e}")
        return [], []
    finally:
        # Fecha o cursor e a conexão para liberar recursos
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obter_operadoras():
    """
    Executa duas consultas: uma para o último trimestre e outra para o último ano,
    e exibe os resultados formatados.
    """
    print("Operadoras com maiores despesas no último trimestre:")
    colunas, resultados_trimestre = consultar_top_operadoras('2024-10-01', '2024-12-31')
    
    if colunas:
        print(" | ".join(colunas))
        for linha in resultados_trimestre:
            print(" | ".join(str(item) for item in linha))
    else:
        print("Nenhum resultado encontrado.")
    
    print("\nOperadoras com maiores despesas no último ano:")
    colunas, resultados_ano = consultar_top_operadoras('2024-01-01', '2024-12-31')
    
    if colunas:
        print(" | ".join(colunas))
        for linha in resultados_ano:
            print(" | ".join(str(item) for item in linha))
    else:
        print("Nenhum resultado encontrado.")
