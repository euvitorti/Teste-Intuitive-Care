import pandas as pd

def transformar_dados(lista_tabelas):
    """
    Transforma e padroniza os dados extraídos das tabelas.
    
    Parâmetros:
        lista_tabelas: Lista de DataFrames extraídos do PDF.
        
    Retorna:
        DataFrame: Tabela única com todos os dados transformados.
    """
    
    # Renomear as colunas
    renomeacao = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }
    
    tabelas_ajustadas = []
    
    # Itera sobre cada DataFrame extraído
    for tabela in lista_tabelas:
        # Reseta o índice da tabela para evitar problemas de concatenação
        tabela.reset_index(drop=True, inplace=True)
        
        # Renomeia as colunas conforme o dicionário de renomeação
        tabela.rename(columns=renomeacao, inplace=True)
        
        # Remove quebras de linha dos nomes das colunas
        tabela.columns = [col.replace("\n", " ") for col in tabela.columns]
        
        # Remove quebras de linha dos dados de colunas do tipo texto
        for col in tabela.select_dtypes(include=['object']).columns:
            tabela[col] = tabela[col].str.replace("\n", " ", regex=False)
        
        # Adiciona a tabela ajustada à lista
        tabelas_ajustadas.append(tabela)
    
    # Concatena todas as tabelas ajustadas em uma única DataFrame
    return pd.concat(tabelas_ajustadas, ignore_index=True)
