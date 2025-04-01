SELECT razao_social, modalidade, uf, telefone, representante, cargo_representante
FROM operadoras_ativas
WHERE razao_social ILIKE %s
LIMIT 10;
