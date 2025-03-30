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
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Levanta exceção para status de erro HTTP
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
    
    # Cria o objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(html, "html.parser")
    links_encontrados = []
    
    # Procura por todas as tags <a> que possuem atributo href
    for link in soup.find_all("a", href=True):
        # Verifica se o texto do link contém algum dos termos desejados
        # e se o link termina com ".pdf"
        if any(termo in link.get_text() for termo in termos_desejados) and link["href"].endswith(".pdf"):
            # Corrige URL relativa para URL absoluta utilizando a função auxiliar
            links_encontrados.append(construir_url(URL_BASE, link["href"]))
            
    return links_encontrados