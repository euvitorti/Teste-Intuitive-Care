import os
import psycopg2
import tempfile
import concurrent.futures
from database.conectar_bd import conectar_banco_de_dados

def importar_csv_individual(caminho_arquivo, tabela, delimitador=';', codificacao='UTF8', caractere_citacao='"'):
    """
    Importa um único arquivo CSV para uma tabela no banco PostgreSQL.

    Parâmetros:
    - caminho_arquivo: Caminho do arquivo CSV.
    - tabela: Nome da tabela de destino no banco.
    - delimitador: Caractere usado para separar as colunas no CSV (padrão: ';').
    - codificacao: Codificação do arquivo (padrão: 'UTF8').
    - caractere_citacao: Caractere que delimita os valores textuais (padrão: '"').
    """
    
    try:
        # Estabelece conexão com o banco de dados usando as configurações importadas
        conexao = conectar_banco_de_dados()
        cursor = conexao.cursor()

        # Lê o conteúdo do arquivo e substitui vírgulas por pontos dos valores presentes na tabela
        with open(caminho_arquivo, 'r', encoding=codificacao) as arquivo:
            conteudo = arquivo.read().replace(',', '.')

        # Cria um arquivo temporário para armazenar o conteúdo modificado
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding=codificacao, suffix='.csv') as arquivo_temp:
            arquivo_temp.write(conteudo)
            caminho_temp = arquivo_temp.name

        # Comando SQL COPY para importar os dados do arquivo CSV para a tabela
        comando_copy = f"""
            COPY {tabela}
            FROM STDIN
            WITH (
                FORMAT CSV,
                HEADER TRUE,
                DELIMITER '{delimitador}',
                QUOTE '{caractere_citacao}'
            )
        """
        
        # Abre o arquivo temporário e executa o comando COPY
        with open(caminho_temp, 'r', encoding=codificacao) as arquivo_temp:
            cursor.copy_expert(sql=comando_copy, file=arquivo_temp)

        # Confirma a transação no banco de dados
        conexao.commit()
        print(f"Arquivo {caminho_arquivo} importado com sucesso para '{tabela}'.")

    except psycopg2.Error as erro:
        # Em caso de erro na operação, exibe a mensagem de erro
        print(f"Erro ao importar {caminho_arquivo}: {erro}")

    finally:
        # Remove o arquivo temporário se ele existir
        if os.path.exists(caminho_temp):
            os.remove(caminho_temp)
        # Fecha o cursor e a conexão com o banco de dados
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def importar_csv_para_tabela_em_paralelo(caminho_pasta, tabela):
    """
    Importa todos os arquivos CSV de uma pasta para a tabela especificada.

    Parâmetros:
    - caminho_pasta: Caminho da pasta que contém os arquivos CSV.
    - tabela: Nome da tabela de destino no banco.
    """
    
    # Lista todos os arquivos com extensão .csv na pasta informada
    arquivos_csv = [os.path.join(caminho_pasta, nome_arquivo) 
                    for nome_arquivo in os.listdir(caminho_pasta) 
                    if nome_arquivo.endswith(".csv")]

    print(f"Iniciando importação de {len(arquivos_csv)} arquivos para a tabela '{tabela}'")
    
    # Define o número máximo de processos
    max_processos = 2

    # Executa a importação em paralelo utilizando ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_processos) as executor:
        # Distribui a função 'importar_csv_individual' com os respectivos argumentos para cada arquivo
        executor.map(importar_csv_individual, arquivos_csv, [tabela] * len(arquivos_csv))

    print("Importação concluída!")
