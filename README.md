# Teste Técnico - Extração, Transformação, Banco de Dados e API

Este projeto consiste em um conjunto de testes técnicos que envolvem Web Scraping, Transformação de Dados, Banco de Dados e API. O objetivo é coletar, estruturar e disponibilizar dados para consultas analíticas e interações via uma API.

---

## Tecnologias Utilizadas

- Python: 3.12.8
- PostgreSQL: (>10.0)
- FastAPI
- Vue.js
- requests: 2.32.3
- beautifulsoup4: 4.13.3

---

## Estrutura do Projeto

Cada módulo do projeto possui sua própria documentação. Leia atentamente para compreender seu funcionamento.

- 📂 **scraping:** Coleta de dados via Web Scraping e download de arquivos.
- 📂 **transformacao:** Extração, tratamento e formatação dos dados coletados.
- 📂 **banco_de_dados:** Estruturação e importação dos dados para o PostgreSQL.
- 📂 **api:** Servidor Python para disponibilizar os dados via endpoints.
- 📂 **tests:** Testes automatizados para garantir qualidade e funcionamento.
- 📂 **intuitive:** Gerenciamento do ambiente virtual e dependências.
- **requirements.txt:** Lista de pacotes necessários para rodar o projeto.
- **README.md:** Documentação principal com instruções de uso.

---

## Como Rodar o Projeto

1. **Configurar o Ambiente Virtual**

    ```bash
        python -m venv intuitive
        source venv/bin/activate  # Linux/Mac
        venv\Scripts\activate     # Windows
        pip install -r requirements.txt
    ```

3. **Configurar o Banco de Dados**

    Certifique-se de que o PostgreSQL está rodando e crie o banco necessário.

psql -U usuario -d meu_banco -f banco_de_dados/schema.sql

3️⃣ Executar os Módulos

🔹 Web Scraping

python scraping/scraper.py

🔹 Transformação de Dados

python transformacao/extracao.py
python transformacao/transformacao.py
python transformacao/exportacao.py

🔹 Importação para o Banco de Dados

python banco_de_dados/importacao.py

🔹 Iniciar a API

uvicorn api.main:app --reload

A API estará disponível em http://localhost:8000.

4️⃣ Testar a API via Postman

Importe a coleção do Postman (postman_collection.json) e execute as requisições.

📂 Documentação dos Módulos

Scraping

Transformação de Dados

Banco de Dados

API

📜 Licença

Este projeto é apenas para fins de teste técnico.