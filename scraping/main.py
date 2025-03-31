from requisicoes.requisicoes import baixar_pagina, extrair_links
from arquivos.arquivos import baixar_arquivos, compactar_arquivos
from config.config import ARQUIVOS_DESEJADOS, URL_BASE, PASTA_DESTINO

def baixar_arquivos_concorrente(links, pasta_destino):
    """
    Baixa os arquivos de forma concorrente.
    
    Parâmetros:
        links: Lista de URLs dos arquivos a serem baixados.
        pasta_destino: Caminho da pasta onde os arquivos serão salvos.

    Retorna:
        list: Lista de caminhos para os arquivos baixados.
    """
    return baixar_arquivos(links, pasta_destino)

def main():
    """
    Função principal executa o fluxo completo:
    1. Baixa o HTML da página.
    2. Extrai os links dos arquivos desejados.
    3. Realiza o download dos arquivos.
    4. Compacta os arquivos baixados.
    """
    html = baixar_pagina(URL_BASE)
    if not html:
        return

    links = extrair_links(html, ARQUIVOS_DESEJADOS)
    arquivos = baixar_arquivos_concorrente(links, PASTA_DESTINO)
    compactar_arquivos(arquivos, PASTA_DESTINO)

if __name__ == "__main__":
    main()
