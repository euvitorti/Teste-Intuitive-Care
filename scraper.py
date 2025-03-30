import requests
from bs4 import BeautifulSoup
import os
import zipfile

# URL da página onde os arquivos estão hospedados
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Faz a requisição para obter o HTML da página
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Lista de textos que identificam os links desejados
arquivos_desejados = ["Anexo I", "Anexo II"]

# Encontra os links pelos textos dentro da tag <a>, filtrando apenas PDFs
download_links = []
for link in soup.find_all("a", href=True):
    if any(nome in link.get_text() for nome in arquivos_desejados) and link["href"].endswith(".pdf"):
        download_links.append(link["href"])

# Criar pasta de downloads, se não existir
os.makedirs("downloads", exist_ok=True)

# Baixa os arquivos encontrados
downloaded_files = []
for link in download_links:
    file_name = link.split("/")[-1]  # Mantém o nome original do arquivo
    file_url = link if link.startswith("http") else url + "/" + link  # Corrige URL se for relativa

    print(f"Baixando {file_name} de {file_url}...")
    file_response = requests.get(file_url)
    
    file_path = f"downloads/{file_name}"
    with open(file_path, "wb") as file:
        file.write(file_response.content)
    
    downloaded_files.append(file_path)

print("Download concluído!")

# Compacta todos os arquivos baixados em um único arquivo ZIP
zip_filename = "downloads/Anexos.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in downloaded_files:
        zipf.write(file, os.path.basename(file))  # Adiciona o arquivo ao zip sem o caminho completo

print(f"Arquivos compactados com sucesso em {zip_filename}")
