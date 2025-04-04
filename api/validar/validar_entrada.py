from fastapi import HTTPException

def validar_termo_busca(termo: str) -> str:
    """
    Valida o termo de busca para garantir que ele seja adequado.

    Regras de validação:
    - Não pode ser vazio.
    - Deve ter pelo menos 2 caracteres.
    - Retorna o termo em maiúsculas.

    :param termo: O termo de busca fornecido pelo usuário.
    :return: O termo validado e convertido para maiúsculas.
    :raises HTTPException: Se o termo for inválido.
    """
    
    # Remove espaços extras e verifica se o termo tem pelo menos 2 caracteres
    termo = termo.strip()
    if len(termo) < 2:
        raise HTTPException(status_code=400, detail="O termo de busca deve ter pelo menos 2 caracteres.")
    
    # Retorna o termo em maiúsculas
    return termo.upper()