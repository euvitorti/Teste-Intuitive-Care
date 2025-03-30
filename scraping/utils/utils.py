from urllib.parse import urljoin

def construir_url(base, link):
    """
    Constrói a URL completa a partir de uma URL base e um link relativo.

    Parâmetros:
        base: URL base.
        link: Link relativo ou absoluto.

    Retorna:
        str: URL completa.
    """
    
    return urljoin(base, link)