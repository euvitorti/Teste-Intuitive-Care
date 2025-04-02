from fastapi import APIRouter, Query, HTTPException
from api.service.api_service import buscar_operadoras
from api.validar.validar_entrada import validar_termo_busca

router = APIRouter()

@router.get("/operadoras/")
def buscar_operadoras_controller(termo: str = Query(..., title="Termo de busca")):
    """
    Endpoint para buscar operadoras pela razão social.

    Parâmetros:
    - termo: Termo de busca fornecido pelo usuário.

    Retorno:
    - JSON com a lista de operadoras encontradas ou uma mensagem de erro.
    """
    
    try:
        termo_validado = validar_termo_busca(termo)
        resultados = buscar_operadoras(termo_validado)

        if not resultados:
            raise HTTPException(status_code=404, detail="Nenhuma operadora encontrada para o termo pesquisado.")

        return {"resultados": resultados}

    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no servidor: {str(e)}")
