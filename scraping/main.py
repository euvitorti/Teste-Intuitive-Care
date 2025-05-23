from requisicoes.requisicoes import baixar_pagina, extrair_links
from arquivos.arquivos import baixar_arquivos, compactar_arquivos
from config.config import ARQUIVOS_DESEJADOS, URL_BASE, PASTA_DESTINO

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
    arquivos = baixar_arquivos(links, PASTA_DESTINO)
    compactar_arquivos(arquivos, PASTA_DESTINO)

if __name__ == "__main__":
    main()
