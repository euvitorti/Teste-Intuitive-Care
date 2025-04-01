import os
import zipfile
import requests
from concurrent.futures import ThreadPoolExecutor

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

    os.makedirs(pasta_destino, exist_ok=True)
    arquivos_baixados = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        for caminho_arquivo in executor.map(lambda link: download_arquivo(link, pasta_destino), links):
            if caminho_arquivo:
                arquivos_baixados.append(caminho_arquivo)

    return arquivos_baixados

def download_arquivo(link, pasta_destino):
    """
    Faz o download de um arquivo a partir de um link.

    Parâmetros:
        link: URL do arquivo.
        pasta_destino: Caminho da pasta onde o arquivo será salvo.

    Retorna:
        str ou None: Caminho do arquivo baixado ou None em caso de erro.
    """
    nome_arquivo = os.path.basename(link)
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    try:
        print(f"Baixando {nome_arquivo} de {link}...")
        response = requests.get(link, timeout=60)
        response.raise_for_status()

        with open(caminho_arquivo, "wb") as file:
            file.write(response.content)
        return caminho_arquivo
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {nome_arquivo}: {e}")
        return None

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

    caminho_zip = os.path.join(pasta_destino, "arquivos_compactados.zip")
    
    try:
        with zipfile.ZipFile(caminho_zip, 'w') as zipf:
            for arquivo in arquivos:
                if os.path.exists(arquivo):
                    zipf.write(arquivo, os.path.basename(arquivo))
                else:
                    print(f"Aviso: {arquivo} não encontrado e não será incluído no ZIP.")
        print(f"Arquivos compactados com sucesso em {caminho_zip}")
        return caminho_zip
    except Exception as e:
        print(f"Erro ao compactar arquivos: {e}")
        return None
