import requests
from bs4 import BeautifulSoup
from config.config import URL_BASE
from utils.utils import construir_url

def baixar_pagina(url):
    """
    Faz a requisição HTTP da página e retorna o conteúdo HTML.

    Parâmetros:
        url: URL da página a ser baixada.

    Retorna:
        str ou None: Conteúdo HTML da página ou None se ocorrer algum erro.
    """
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None

def extrair_links(html, termos_desejados):
    """
    Extrai os links dos arquivos PDF que contenham os termos desejados no texto do link.

    Parâmetros:
        html: Conteúdo HTML da página.
        termos_desejados: Nome dos arquivos que devem estar presentes no texto do link.

    Retorna:
        list: Lista de URLs completas dos arquivos PDF encontrados.
    """
    soup = BeautifulSoup(html, "html.parser")
    links_encontrados = []

    for link in soup.find_all("a", href=True):
        if any(termo in link.get_text() for termo in termos_desejados) and link["href"].endswith(".pdf"):
            links_encontrados.append(construir_url(URL_BASE, link["href"]))
    
    return links_encontrados
