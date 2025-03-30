# Extrator, Transformador e Compactador de Dados

Este projeto realiza a extração de tabelas de um arquivo PDF, transforma os dados extraídos para padronização e limpeza, salva as informações em um arquivo CSV e, por fim, compacta o arquivo processado em um ZIP.

---

## AVISO

O projeto utiliza a biblioteca tabula, que necessita do Java instalado e configurado corretamente na variável de ambiente (path). Com isso, o script poderá ser executado sem problemas.

---

## Funcionalidades

1. **Extração de dados:** Obtém tabelas a partir de um arquivo PDF especificado.
2. **Transformação dos dados:** Padroniza os dados extraídos, ajustando colunas e removendo caracteres indesejados.
3. **Salvamento em CSV:** Gera um arquivo CSV com os dados estruturados.
4. **Compactação dos arquivos:** O arquivo CSV gerado é compactado em um arquivo ZIP.

---

## Tecnologias Utilizadas

- Python 3
- Pandas (para manipulação de tabelas)
- Tabula (para extração de tabelas de PDFs)
- os, zipfile (para manipulação de arquivos e compactação)

---

## Estrutura do Projeto

- 📁 **config/config.py:** Configurações globais do projeto
- 📁 **extrair/extrair.py:** Responsável por extrair tabelas do PDF
- 📁 **arquivos/arquivos.py:** Gerencia download e compactação de arquivos
- 📁 **transformador/transformador.py:** Realiza a transformação e padronização dos dados extraídos
- 📁 **salvar/salvar.py:** Salva os dados em um CSV e compacta o arquivo gerado
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
    O programa irá extrair, transformar, salvar e compactar os dados automaticamente.
`