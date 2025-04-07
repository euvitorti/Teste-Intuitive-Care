import pytest
from fastapi import HTTPException
from api.src.validar.validar_entrada import validar_termo_busca

# Teste de entrada válida
@pytest.mark.parametrize("input_term,expected", [
    ("operadora", "OPERADORA"),
    ("  banco  ", "BANCO"),
    ("Ab", "AB"),
    ("c1", "C1"),
    ("teste123", "TESTE123"),
])
def test_validar_termo_busca_valida(input_term, expected):
    assert validar_termo_busca(input_term) == expected

# Testes de entradas inválidas
@pytest.mark.parametrize("input_term", [
    "",      # vazio
    " ",     # só espaço
    "a",     # um caractere
    "  a ",  # um caractere com espaço
])
def test_validar_termo_busca_invalida(input_term):
    with pytest.raises(HTTPException) as exc:
        validar_termo_busca(input_term)
    assert exc.value.status_code == 400
    assert "pelo menos 2 caracteres" in exc.value.detail
