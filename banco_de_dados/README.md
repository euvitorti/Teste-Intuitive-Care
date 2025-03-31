# Módulo de Integração e Consulta de Dados com PostgreSQL

Este módulo tem como objetivo criar, popular e consultar tabelas em um banco de dados PostgreSQL.

---

## Funcionalidades

1. **Criação de Tabelas:** Lê um arquivo SQL contendo os comandos para criação das tabelas necessárias e executa estes comandos no banco de dados.
2. **Importação de Dados:** Importa arquivos CSV para as tabelas correspondentes de forma paralela. São utilizadas duas funções:
    - **importar_csv_individual:** Importa um único arquivo CSV para a tabela especificada. Durante a importação, o conteúdo é processado e um comando SQL COPY é utilizado para inserir os dados.
    - **importar_csv_para_tabela_em_paralelo:** Percorre uma pasta específica, identifica todos os arquivos CSV e os importa em paralelo utilizando um ProcessPoolExecutor com um número máximo fixo de processos (2, que pode ser modificado conforme a necessidade).

3. **Consulta dos Dados:** Executa queries SQL para obter os dados desejados. Por exemplo, a função consultar_top_operadoras lê um arquivo SQL (localizado em sql/consultar_operadoras.sql) e consulta as 10 operadoras com maiores despesas dentro de um intervalo de datas.
4. **Conexão com o Banco de Dados:** A conexão é realizada através da biblioteca psycopg2 e utiliza um arquivo de configuração (db_config) que define os parâmetros de conexão.

    Por padrão, o script utiliza as configurações:

    ```
        host: localhost
        database: intuitive
        user: postgres
        password: root
    ```

    `
        Atualize o arquivo db_config/db_config.py com os parâmetros de conexão do seu banco de dados.
    `

---

## Tecnologias Utilizadas

- **Python 3**
- **Banco de Dados PostgreSQL:** 16.8.1
- **psycopg2:** Biblioteca responsável por realizar a conexão com oPostgreSQL.

---

## Estrutura do Projeto

- 📁 **criar_tabelas/criar_tabelas.py:** Função para criação das tabelas
- 📁 **importar_data/importar_data.py**: Funções para importação dos arquivos CSV
- 📁 **consultar_tabelas/consultar_tabelas.py:** Funções para consultar os dados das tabelas
- 📁 **db_config/db_config.py:** Configuração do banco de dados PostgreSQL
- 📁 **sql/criar_tabelas.sql e consultar_operadoras.sql:** Script para criação e consulta das tabelas
- 📁 **tabelas:** Pasta com os CSV para popular as tabelas
- **main.py:** Script principal que executa o fluxo completo
- **README.md:** Documentação do projeto

---

## Arquivos SQL e CSV

- **SQL:** O script utiliza dois arquivos SQL principais:
    - **criar_tabelas.sql:** Responsável por criar as tabelas demonstracoes_contabeis e operadoras_ativas.
    - **consultar_operadoras.sql:** Contém a query que consulta as 10 operadoras com maiores despesas em um determinado intervalo de datas.

- **CSV:** Os arquivos CSV localizados nas pastas tabelas/demonstracoes_contabeis e tabelas/operadoras_de_plano_de_saude_ativas são importados para as respectivas tabelas.

---

## Como Usar

1. **Executar o Script:**

    Basta rodar o script principal:

    ```
        python main.py
    ```

    - Isso fará com que:
        - As tabelas sejam criadas a partir do arquivo SQL.
        - Os arquivos CSV sejam importados para as tabelas.
        - As consultas sejam realizadas e os resultados exibidos no terminal.

---

## Personalização e Modificações

- **Paralelismo na Importação:** Se desejar alterar o número máximo de processos utilizados para a importação dos CSVs, modifique a variável max_processos na função importar_csv_para_tabela_em_paralelo.

---

### Conclusão

Este módulo integra diversas funcionalidades para a gestão de dados: criação de tabelas, importação paralela de arquivos CSV e execução de consultas SQL. A modularidade do código permite que cada componente seja facilmente alterado ou expandido, atendendo a diferentes necessidades de usuário e configurações de ambiente.
