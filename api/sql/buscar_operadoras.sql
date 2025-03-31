SELECT razao_social, modalidade, uf, telefone, representante, cargo_representante, cnpj
FROM operadoras_ativas
WHERE razao_social ILIKE %s
LIMIT 10;
