from requisicoes.requisicoes import baixar_pagina, extrair_links
from arquivos.arquivos import baixar_arquivos, compactar_arquivos
from config.config import ARQUIVOS_DESEJADOS, URL_BASE, PASTA_DESTINO

def main():
    """
    Função principal que orquestra o fluxo completo:
    1. Baixa o HTML da página.
    2. Extrai os links dos arquivos desejados.
    3. Realiza o download dos arquivos.
    4. Compacta os arquivos baixados.
    """
    
    # Baixa o conteúdo HTML da URL base
    html = baixar_pagina(URL_BASE)
    if not html:
        return
    
    # Extrai os links dos arquivos PDF que contêm os termos desejados
    links = extrair_links(html, ARQUIVOS_DESEJADOS)
    # Baixa os arquivos a partir dos links encontrados
    arquivos = baixar_arquivos(links, PASTA_DESTINO)
    # Compacta os arquivos baixados em um arquivo ZIP
    compactar_arquivos(arquivos, PASTA_DESTINO)

if __name__ == "__main__":
    main()