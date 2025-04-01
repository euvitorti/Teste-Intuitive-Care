| Nome do Teste                        | Método | URL                                                 | Parâmetro (termo)                                  | Esperado |
|--------------------------------------|--------|------------------------------------------------------|----------------------------------------------------|----------|
| DEVE_RETORNAR_DADO                   | GET    | http://127.0.0.1:8000/operadoras/?termo=...         | 18 DE JULHO ADMINISTRADORA DE BENEFÍCIOS LTDA      | Dados encontrados |
| DEVE_RETORNAR_DADO_PARAM_COM_ESPAÇO  | GET    | http://127.0.0.1:8000/operadoras/?termo=...         |  2B ODONTOLOGIA OPERADORA DE PLANOS ODONTOLÓGICOS LTDA  | Dados encontrados |
| DEVE_OCORRER_ERRO_PARAM_INSUFICIENTE | GET    | http://127.0.0.1:8000/operadoras/?termo=1           | 1                                                  | Erro: caracteres insuficientes |
| DEVE_OCORRER_ERRO_CAMPO_VAZIO        | GET    | http://127.0.0.1:8000/operadoras/?termo=            | (vazio)                                            | Erro: termo ausente |
| DEVE_OCORRER_ERRO_EMPRESA_INEXISTENTE| GET    | http://127.0.0.1:8000/operadoras/?termo=EMPRESA_INEXISTENTE | EMPRESA_INEXISTENTE                           | Erro: empresa não existe |
