# Baixador e Compactador de Arquivos PDF

Este projeto realiza o download de arquivos PDF a partir de uma página web específica, filtra os arquivos desejados com base em termos-chave, e compacta os arquivos baixados em um arquivo ZIP.

---

## Funcionalidades

1. Acessa uma URL específica e baixa seu conteúdo HTML.
2. Extrai links de arquivos PDF que contenham palavras-chave predefinidas.
3. Baixa os arquivos encontrados e os armazena localmente.
4. Compacta os arquivos baixados em um único arquivo ZIP.

---

## Tecnologias Utilizadas

- Python 3
- Requests (para fazer requisições HTTP)
- BeautifulSoup (para extração de links do HTML)
- os, zipfile (para manipulação de arquivos e compactação)

---

## Estrutura do Projeto

- 📁 **config/config.py:** Configurações globais do projeto
- 📁 **requisicoes/requisicoes.py:** Lida com requisições HTTP e extração de links
- 📁 **arquivos/arquivos.py:** Gerencia download e compactação de arquivos
- 📁 **utils/utils.py:** Funções auxiliares (como construir URLs)
- **main.py:** Script principal que executa o fluxo completo
- **README.md:** Documentação do projeto

---

## Como Usar

1. **Execute o script principal**

    ```
        python main.py
    ```
---

`
    O programa irá baixar os arquivos correspondentes e compactá-los automaticamente.
`