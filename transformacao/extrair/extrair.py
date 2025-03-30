import tabula

def extrair_dados_pdf(arquivo_pdf, paginas):
    """
    Extrai tabelas do PDF utilizando a biblioteca Tabula.
    
    Parâmetros:
        arquivo_pdf: Caminho do arquivo PDF.
        paginas: Intervalo de páginas a ser extraído.
        
    Retorna:
        list: Lista de DataFrames contendo as tabelas extraídas.
    """
    return tabula.read_pdf(
        arquivo_pdf,
        pages=paginas,
        multiple_tables=True,
        encoding="latin1",
        lattice=True
    )
    