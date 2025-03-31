from criar_tabelas.criar_tabelas import criar_tabelas
from importar_data.importar_data import importar_csv_para_tabela_em_paralelo
from consultar_tabelas.consultar_tabelas import obter_operadoras

def main():
    """
    Função principal que executa as seguintes etapas:
      1. Cria as tabelas no banco de dados a partir de um arquivo SQL.
      2. Importa os arquivos CSV para as tabelas correspondentes de forma paralela.
    """
    
    # Caminho do arquivo SQL contendo os comandos para criação das tabelas.
    arquivo_sql = "sql/criar_tabelas.sql"
    criar_tabelas(arquivo_sql)

    # Caminho da pasta com os arquivos CSV para a tabela 'demonstracoes_contabeis'.
    pasta_demonstracoes = "tabelas/demonstracoes_contabeis"
    
    # Importa os arquivos CSV para a tabela 'demonstracoes_contabeis' de forma paralela.
    importar_csv_para_tabela_em_paralelo(pasta_demonstracoes, "demonstracoes_contabeis")

    # Caminho da pasta com os arquivos CSV para a tabela 'operadoras_ativas'.
    pasta_operadoras = "tabelas/operadoras_de_plano_de_saude_ativas"
    
    # Importa os arquivos CSV para a tabela 'operadoras_ativas' de forma paralela.
    importar_csv_para_tabela_em_paralelo(pasta_operadoras, "operadoras_ativas")
    
    # Consultar as 10 operadoras com maiores despesas
    obter_operadoras()

if __name__ == '__main__':
    main()
