# Teste Técnico - Extração, Transformação, Banco de Dados, API e FrontEnd

Este projeto consiste em um conjunto de testes técnicos que envolvem Web Scraping, Transformação de Dados, Banco de Dados, API e FrontEnd. O objetivo é coletar, estruturar e disponibilizar dados para consultas analíticas e interações via uma API.

---

### Acesse a Aplicação em Produção (Frontend + API)

Em vez de testar o módulo frontend e da api localmente, você pode testar **o frontend em Vue** consumindo diretamente a **API em FastAPI**, ambos hospedados na Vercel:

- **[Acessar Frontend (Vue.js)](https://intuitive-vitor.vercel.app/)**  

> Toda a comunicação entre frontend e backend já está configurada. Ao buscar uma operadora, o frontend faz requisições HTTP para a API em produção, que retorna os dados estruturados do banco de dados PostgreSQL.

---

## Tecnologias Utilizadas

- Python: 3.12.8
- PostgreSQL: 16.8.1
- FastAPI: 0.115.12
- Vue.js: 3.5.13
- requests: 2.32.3
- beautifulsoup4: 4.13.3
- pandas: 2.2.3
- tabula-py: 2.10.0
- psycopg2: 2.9.10

---

## Arquitetura e Princípios de Projeto

O projeto foi desenvolvido seguindo uma arquitetura em camadas e modular, que facilita a manutenção, a escalabilidade e o teste dos componentes individuais. Em cada módulo, foram aplicados os seguintes princípios:

- **Single Responsibility Principle (SRP):**  
  Cada módulo (scraping, transformação, banco de dados, API e frontend) foi projetado para ter uma única responsabilidade bem definida, garantindo que as mudanças em uma funcionalidade não afetem outras partes do sistema.

- **Separation of Concerns:**  
  As diferentes camadas – extração e transformação de dados, persistência em banco de dados, e exposição via API – estão claramente separadas. Isso possibilita que cada parte do sistema seja desenvolvida e aprimorada de forma independente.

- **Modularidade:**  
  A estrutura em módulos permite que cada parte do projeto tenha sua própria documentação e ciclo de desenvolvimento. Essa abordagem facilita a reutilização de componentes e a integração de novas funcionalidades.

- **Escalabilidade:**  
  A combinação de tecnologias modernas (FastAPI para a API, Vue.js para o frontend e PostgreSQL para o banco de dados) e a separação clara das responsabilidades contribui para a escalabilidade e evolução contínua do projeto.

Esta arquitetura e a aplicação dos princípios SOLID garantem um código mais organizado, testável e fácil de manter, atendendo aos requisitos dos testes técnicos de Extração, Transformação, Banco de Dados e API.

- 📂 **api:** Servidor Python para disponibilizar os dados via endpoints.
- 📂 **banco_de_dados:** Estruturação e importação dos dados para o PostgreSQL.
- 📂 **intuitiveFront:** Frontend que faz a conexão com a api.
- 📂 **scraping:** Coleta de dados via Web Scraping e download de arquivos.
- 📂 **transformacao:** Extração, tratamento e formatação dos dados coletados.
- **requirements.txt:** Lista de pacotes necessários para rodar o projeto.
- **README.md:** Documentação principal com instruções de uso.

---

## Configurar o Projeto

1. **Configurar o Ambiente Virtual**

    ```bash
        python -m venv intuitive
        source venv/bin/activate  # Linux/Mac
        intuitive\Scripts\activate     # Windows
        pip install -r requirements.txt
    ```

2. **Configurar o Banco de Dados**

    Certifique-se de que o PostgreSQL está rodando e crie o banco necessário, pois vamos precisar para a configuração no módulo Banco de Dados.

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
- [Front](intuitiveFront/README.md)
- [Postman](api/postman/README.md)

---

`
     Está estudando ou se inspirando neste projeto? Deixe uma estrela e compartilhe comigo, vou gostar de ver o que você está construindo!
`
