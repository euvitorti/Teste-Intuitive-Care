# Módulo de Busca de Operadoras com FastAPI e PostgreSQL

Este módulo tem como objetivo realizar consultas de operadoras por meio de uma API desenvolvida em FastAPI, utilizando um banco de dados PostgreSQL.

---

### 💡 Você pode testar a aplicação diretamente, sem rodar localmente, acessando: [Site](https://intuitive-vitor.vercel.app/)

---

## Funcionalidades

1. **Endpoint:** Um endpoint GET (/operadoras/) está disponível para que os usuários realizem consultas sobre operadoras de saúde.

2. **Validação de Termo de Busca:** Antes da execução da busca, o termo passado pelo usuário é validado para garantir que:
    - Não seja vazio.
    - Possua pelo menos 2 caracteres.
    - Seja convertido para maiúsculas.

3. **Consulta ao Banco de Dados:** A API executa queries no PostgreSQL para buscar operadoras com base no termo de busca informado pelo usuário.

4. A query SQL é carregada de um arquivo externo localizado na pasta sql.

5. **Tratamento de Exceções:**
    - Retorna HTTP 400 caso o termo de busca seja inválido.
    - Retorna HTTP 404 caso nenhuma operadora seja encontrada.
    - Retorna HTTP 500 para erros internos do servidor.

6. **Conexão com o Banco de Dados:** A conexão é realizada através da biblioteca psycopg2 e utiliza um arquivo de configuração (db_config) que define os parâmetros de conexão.

    Por padrão, o script utiliza as configurações:

    ```
        host: localhost
        database: intuitive
        user: postgres
        password: root
    ```

    `
        Atualize o arquivo banco_de_dados_db_config/db_config.py com os parâmetros de conexão do seu banco de dados.
    `

---

## Tecnologias Utilizadas

- **Python 3**
- **Banco de Dados PostgreSQL:** 16.8.1
- **psycopg2:** Biblioteca responsável por realizar a conexão com oPostgreSQL.
- **FastAPI:** Framework para desenvolvimento da API
- **uvicorn:** Servidor para execução da API

---

## Estrutura do Projeto

A aplicação foi organizada em camadas seguindo boas práticas de separação de responsabilidades. Abaixo está o mapeamento das pastas e seus propósitos:

```
.
├── README.md                # Documentação principal do projeto
├── postman/                 # Recursos para testes com Postman
│   ├── README.md            # Explicação sobre importação da coleção
│   ├── curl/                # Coleção Postman (JSON)
│   └── img/                 # Imagens ilustrativas do Postman
│
├── src/                     # Código-fonte da aplicação
│   ├── main.py              # Ponto de entrada da aplicação FastAPI
│   │
│   ├── rotas/               # Camada de controle (rotas)
│   │   └── operadora_controller.py  # Endpoint principal: /operadoras/
│   │
│   ├── service/             # Camada de serviço (regras de negócio)
│   │   └── api_service.py   # Lógica para buscar operadoras no banco
│   │
│   ├── sql/                 # Consultas SQL
│   │   └── buscar_operadoras.sql  # Query utilizada na busca por operadoras
│   │
│   └── validar/             # Camada de validação de entrada
│       └── validar_entrada.py  # Função para validar e padronizar o termo de busca
│
└── tests/                   # Testes automatizados
    │
    └── validar/             # Testes da camada de validação
        └── test_validar_entrada.py
```

### Destaques

- **Modularização clara:** Cada responsabilidade (rota, serviço, validação, SQL) está separada, facilitando a manutenção e escalabilidade.
- **Testes bem estruturados:** Os testes foram organizados por domínio (validar), com uso de classes e pytest para garantir robustez.
- **Recursos extras:** A pasta postman fornece tudo que o usuário precisa para testar a API com interface gráfica.

---

## Como Usar Localmente

1. **Executar o Script:**

    Basta rodar o script principal:

    ```
        uvicorn api.src.main:app --reload
    ```
    Certifique-se de estar na pasta raiz (Teste-Intuitive-Care) do projeto.

2. **Fazer uma requisição ao endpoint:**
    Acesse a coleção no [Postman](postman/README.md) e faça a importação.

---

## Testes Automatizados

Foram adicionadas de testes para validar se o módulo de validação de entrada (validar_entrada.py) está funcionando conforme o esperado. Essa abordagem organiza os cenários de teste e assegura a integridade do código com futuras alterações. 

- **Os testes abordam:**
    - **Entradas válidas:** Verifica se o termo de busca é devidamente transformado para maiúsculas e sem espaços extras.
    - **Entradas inválidas:** Garante que entradas inválidas (por exemplo, termos vazios ou com menos de 2 caracteres) disparem uma exceção apropriada (HTTPException com status 400).

    **Para rodar os testes, basta executar o seguinte comando em qualquer pasta do projeto:**
    ```
        pytest -q
    ```

---

### Conclusão

Este módulo fornece uma API rápida e eficiente para buscar operadoras no banco de dados PostgreSQL. O código está estruturado de forma modular para facilitar manutenção e expansão futura.