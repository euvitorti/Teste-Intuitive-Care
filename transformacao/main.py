from extrair.extrair import extrair_dados_pdf
from transformador.transformador import transformar_dados
from salvar.salvar import salvar_csv, compactar_arquivo
from config.config import ARQUIVO_PDF, PAGINAS, CSV_NAME, ZIP_NAME

def main():
    """
    Executa o fluxo completo do processamento:
      1. Extrai dados do PDF.
      2. Transforma e padroniza os dados extraídos.
      3. Salva os dados transformados em um arquivo CSV.
      4. Compacta o arquivo CSV em um arquivo ZIP.
    """
    
    # Extrai as tabelas do arquivo PDF
    lista_tabelas = extrair_dados_pdf(ARQUIVO_PDF, PAGINAS)
    
    # Transforma e padroniza as tabelas extraídas
    tabela_transformada = transformar_dados(lista_tabelas)
    
    # Salva a tabela transformada em um arquivo CSV
    salvar_csv(tabela_transformada, CSV_NAME)
    
    # Compacta o arquivo CSV gerado em um arquivo ZIP
    compactar_arquivo(CSV_NAME, ZIP_NAME)

if __name__ == "__main__":
    main()
    