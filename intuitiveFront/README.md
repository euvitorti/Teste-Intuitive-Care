# Projeto Vue

Este módulo é uma aplicação frontend desenvolvida em Vue.js com Vite e um backend em FastAPI. O frontend faz uma requisição à API para buscar operadoras, e o backend se comunica com um banco de dados para retornar os resultados.

---

## O que o frontend faz

1. A interface do usuário permite que o usuário faça uma busca por operadoras através de um termo.
2. A busca é realizada enviando uma requisição GET para o backend, que retorna uma lista de operadoras.

---

## Pré-requisitos

- Node.js
- [Servidor BackEnd](../api/README.md)

---

## Como rodar

1. **Rodando o Backend (FastAPI):** Antes de rodar o frontend, é necessário que a API (backend) esteja rodando. O backend é responsável por processar as requisições feitas pelo frontend.

2. **Navegue para a pasta do backend:**

    ```
        cd Teste-Intuitive-Care\intuitiveFront
    ```

3. **Rodando o Frontend (Vue + Vite):**
    Instale as dependências do frontend:
    ```
        npm install
    ```
    Rode o servidor de desenvolvimento do frontend:

    ```
        npm run dev
    ```

    `
        O frontend estará disponível em http://localhost:5173.
    `

---

## Considerações Finais

Este projeto depende da API estar rodando para funcionar corretamente. A interface do frontend faz requisições ao backend para buscar os dados e exibi-los ao usuário.