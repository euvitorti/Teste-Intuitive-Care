from fastapi import FastAPI, Query, HTTPException
from api.service.api_service import buscar_operadoras
from api.validar.validar_entrada import validar_termo_busca

# Inicializa a aplicação FastAPI
app = FastAPI()

@app.get("/operadoras/")
def buscar_operadoras_controller(termo: str = Query(..., title="Termo de busca")):
    """
    Endpoint para buscar operadoras pela razão social.

    Parâmetros:
    - termo: Termo de busca fornecido pelo usuário.

    Retorno:
    - JSON com a lista de operadoras encontradas ou uma mensagem de erro.
    """
    
    try:
        # Valida o termo antes de executar a busca
        termo_validado = validar_termo_busca(termo)

        # Chama o serviço para buscar no banco de dados
        resultados = buscar_operadoras(termo_validado)

        # Se não houver resultados, lança uma exceção HTTP 404
        if not resultados:
            raise HTTPException(status_code=404, detail="Nenhuma operadora encontrada para o termo pesquisado.")

        # Retorna os resultados encontrados
        return {"resultados": resultados}

    except HTTPException as http_error:
        # Tratar exceções HTTP conhecidas (ex: termo inválido ou não encontrado)
        raise http_error
    except Exception as e:
        # Captura erros inesperados e retorna um erro 500
        raise HTTPException(status_code=500, detail=f"Erro interno no servidor: {str(e)}")
