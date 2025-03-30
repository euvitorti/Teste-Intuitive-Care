# import zipfile
# import os
# import tabula
# import pandas as pd

# # Extração do PDF usando lattice
# lista_tabelas = tabula.read_pdf(
#     "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
#     pages="1-181",  
#     multiple_tables=True,
#     encoding="latin1",
#     lattice=True
# )

# renomeacao = {
#     'OD': 'Seg. Odontológica',
#     'AMB': 'Seg. Ambulatorial'
# }

# tabelas_ajustadas = []

# for tabela in lista_tabelas:
#     tabela.reset_index(drop=True, inplace=True)
#     # Renomeia as colunas conforme necessário
#     tabela.rename(columns=renomeacao, inplace=True)
#     # Remove quebras de linha dos nomes das colunas
#     tabela.columns = [col.replace("\n", " ") for col in tabela.columns]
#     # Remove quebras de linha dos dados das células (para colunas do tipo string)
#     for col in tabela.select_dtypes(include=['object']).columns:
#         tabela[col] = tabela[col].str.replace("\n", " ", regex=False)
#     tabelas_ajustadas.append(tabela)

# # Concatenando as tabelas extraídas, se houver mais de uma
# tabela_final = pd.concat(tabelas_ajustadas, ignore_index=True)

# # Salvando a tabela final em um CSV usando ";" como delimitador
# csv_name = 'dados_estruturados.csv'
# tabela_final.to_csv(csv_name, index=False, sep=";", encoding='utf-8-sig')

# print("CSV gerado com sucesso!")

# # Nome do arquivo CSV gerado
# csv_name = 'dados_estruturados.csv'

# # Nome do arquivo ZIP
# zip_name = f'Teste_João_Vítor_Santos_Lima.zip'

# # Compactando o CSV em um arquivo ZIP
# with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
#     zipf.write(csv_name, os.path.basename(csv_name))

# print(f"Arquivo {zip_name} compactado com sucesso!")
