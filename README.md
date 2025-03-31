# Teste Técnico - Extração, Transformação, Banco de Dados e API

Este projeto consiste em um conjunto de testes técnicos que envolvem Web Scraping, Transformação de Dados, Banco de Dados e API. O objetivo é coletar, estruturar e disponibilizar dados para consultas analíticas e interações via uma API.

---

## Tecnologias Utilizadas

- Python: 3.12.8
- PostgreSQL: 16.8.1
- FastAPI
- Vue.js
- requests: 2.32.3
- beautifulsoup4: 4.13.3
- pandas: 2.2.3
- tabula-py: 2.10.0
- psycopg2: 2.9.10

---

## Estrutura do Projeto

Cada módulo do projeto possui sua própria documentação.

- 📂 **scraping:** Coleta de dados via Web Scraping e download de arquivos.
- 📂 **transformacao:** Extração, tratamento e formatação dos dados coletados.
- 📂 **banco_de_dados:** Estruturação e importação dos dados para o PostgreSQL.
- 📂 **api:** Servidor Python para disponibilizar os dados via endpoints.
- 📂 **tests:** Testes automatizados para garantir qualidade e funcionamento.
- 📂 **intuitive:** Gerenciamento do ambiente virtual e dependências.
- **requirements.txt:** Lista de pacotes necessários para rodar o projeto.
- **README.md:** Documentação principal com instruções de uso.

---

## Configurar o Projeto

1. **Configurar o Ambiente Virtual**

    ```bash
        python -m venv intuitive
        source venv/bin/activate  # Linux/Mac
        venv\Scripts\activate     # Windows
        pip install -r requirements.txt
    ```

2. **Configurar o Banco de Dados**

    Certifique-se de que o PostgreSQL está rodando e crie o banco necessário, pois vamos precisar para a configuração do módulo Banco de Dados.

3. **Executar os Módulos**

    Depois de configurar o ambiente e ter feito o download das bibliotecas, navegue pelas pasta e acesse a documentação do respectivo módulo de como rodar e as suas responsabilidades.

4. **Executar o comando principal**

    Ao executar:

    ```
        python main.py
    ```
    Certifique-se de estar na pasta do projeto em questão.

---

## Documentação dos Módulos

- [Scraping](scraping/README.md)
- [Transformação de Dados](transformacao/README.md)
- [Banco de Dados](banco_de_dados/README.md)
- [API](api/README.md)

---

Este projeto é apenas para fins de teste técnico.