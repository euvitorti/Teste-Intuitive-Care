import os

# Define o caminho do arquivo PDF a ser processado.
ARQUIVO_PDF = os.path.join("..", "scraping", "dados_baixados", "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")

# Define as páginas do PDF de onde os dados serão extraídos.
PAGINAS = "3-181"

# Pasta onde os arquivos processados serão salvos.
PASTA_DESTINO = os.path.join("dados_processados")

# Cria a pasta de destino se ela não existir.
os.makedirs(PASTA_DESTINO, exist_ok=True)

# Define o nome completo (com caminho) do arquivo CSV a ser gerado.
CSV_NAME = os.path.join(PASTA_DESTINO, "dados_estruturados.csv")

# Define o nome completo (com caminho) do arquivo ZIP a ser gerado.
ZIP_NAME = os.path.join(PASTA_DESTINO, "Teste_João_Vítor_Santos_Lima.zip")
