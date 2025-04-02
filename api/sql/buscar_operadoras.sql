SELECT 
    razao_social, 
    nome_fantasia, 
    cnpj, 
    modalidade, 
    cidade, 
    uf, 
    telefone, 
    endereco_eletronico, 
    data_registro_ans
FROM operadoras_ativas
WHERE razao_social ILIKE %s
LIMIT 10;
