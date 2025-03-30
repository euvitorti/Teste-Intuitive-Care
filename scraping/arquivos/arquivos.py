import os
import zipfile
import requests
from config.config import PASTA_DESTINO

def baixar_arquivos(links, pasta_destino):
    """
    Baixa os arquivos a partir de uma lista de links e os salva na pasta especificada.

    Parâmetros:
        links: Lista de URLs dos arquivos a serem baixados.
        pasta_destino: Caminho da pasta onde os arquivos serão salvos.

    Retorna:
        list: Lista com os caminhos dos arquivos baixados.
    """
    
    if not links:
        print("Nenhum link encontrado para download.")
        return []

    # Cria a pasta de destino caso ela não exista
    os.makedirs(pasta_destino, exist_ok=True)
    arquivos_baixados = []
    
    # Itera sobre cada link para fazer o download
    for link in links:
        # Extrai o nome do arquivo a partir do link
        nome_arquivo = os.path.basename(link)
        # Define o caminho completo para salvar o arquivo
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

        try:
            print(f"Baixando {nome_arquivo} de {link}...")
            # Realiza a requisição para baixar o arquivo
            response = requests.get(link, timeout=10)
            # Tratando erro caso a requisição não for bem sucedida
            response.raise_for_status()

            # Salva o conteúdo do arquivo no caminho especificado
            with open(caminho_arquivo, "wb") as file:
                file.write(response.content)

            # Adiciona o caminho do arquivo baixado à lista
            arquivos_baixados.append(caminho_arquivo)
        except IOError as e:
            # Em caso de erro ao salvar o arquivo, imprime uma mensagem de erro
            print(f"Erro ao salvar {nome_arquivo}: {e}")
    
    return arquivos_baixados

def compactar_arquivos(arquivos, pasta_destino):
    """
    Compacta os arquivos baixados em um único arquivo ZIP.

    Parâmetros:
        arquivos: Lista com os caminhos dos arquivos a serem compactados.
        pasta_destino: Caminho da pasta onde o arquivo ZIP será salvo.

    Retorna:
        str ou None: Caminho do arquivo ZIP criado ou None em caso de erro.
    """
    
    if not arquivos:
        print("Nenhum arquivo para compactar.")
        return None

    # Define o caminho para o arquivo ZIP que será criado
    caminho_zip = os.path.join(pasta_destino, "arquivos_compactados.zip")
    
    try:
        # Cria o arquivo ZIP
        with zipfile.ZipFile(caminho_zip, 'w') as zipf:
            # Itera sobre cada arquivo na lista
            for arquivo in arquivos:
                # Verifica se o arquivo existe antes de adicioná-lo ao ZIP
                if os.path.exists(arquivo):
                    # Adiciona o arquivo ao ZIP com seu nome base
                    zipf.write(arquivo, os.path.basename(arquivo))
                else:
                    print(f"Aviso: {arquivo} não encontrado e não será incluído no ZIP.")
        print(f"Arquivos compactados com sucesso em {caminho_zip}")
        return caminho_zip
    except Exception as e:
        # Em caso de erro durante a compactação, informa o usuário e retorna None
        print(f"Erro ao compactar arquivos: {e}")
        return None