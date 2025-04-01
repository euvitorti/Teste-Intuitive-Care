# Módulo de Busca de Operadoras com FastAPI e PostgreSQL

Este módulo tem como objetivo realizar consultas de operadoras por meio de uma API desenvolvida em FastAPI, utilizando um banco de dados PostgreSQL.

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

- 📁 **service/api_service.py:** Contém a função buscar_operadoras que realiza a consulta no banco.
- 📁 **validar/validar_entrada.py:** Função validar_termo_busca que verifica e padroniza o termo de busca.
- 📁 **sql/buscar_operadoras.sql:** Contém a query SQL utilizada para a busca de operadoras.
- **main.py:** Arquivo principal que inicia a API FastAPI.
- **README.md:** Documentação do projeto.

---

## Como Usar

1. **Executar o Script:**

    Basta rodar o script principal:

    ```
        uvicorn api.main:app --reload
    ```
    Certifique-se de estar na pasta raiz (Teste-Intuitive-Care) do projeto.

2. **Fazer uma requisição ao endpoint:**
    Acesse a coleção no [Postman](/Postman) e faça a importação.

---


### Conclusão

Este módulo fornece uma API rápida e eficiente para buscar operadoras no banco de dados PostgreSQL. O código está estruturado de forma modular para facilitar manutenção e expansão futura.