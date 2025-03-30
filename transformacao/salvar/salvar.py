import zipfile
import os

def salvar_csv(tabela, nome_arquivo):
    """
    Salva a tabela transformada em um arquivo CSV na pasta de destino.
    
    Parâmetros:
        tabela (DataFrame): Tabela a ser salva.
        nome_arquivo (str): Caminho completo do arquivo CSV a ser gerado.
    """
    tabela.to_csv(nome_arquivo, index=False, sep=";", encoding='utf-8-sig')
    print(f"CSV salvo em: {nome_arquivo}")

def compactar_arquivo(arquivo_origem, arquivo_zip):
    """
    Compacta um arquivo em formato ZIP na pasta de destino.
    
    Parâmetros:
        arquivo_origem: Caminho do arquivo que será compactado.
        arquivo_zip: Caminho completo do arquivo ZIP a ser gerado.
    """
    with zipfile.ZipFile(arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o arquivo ao ZIP, mantendo apenas o nome base do arquivo
        zipf.write(arquivo_origem, os.path.basename(arquivo_origem))
    print(f"Arquivo ZIP salvo em: {arquivo_zip}")
    