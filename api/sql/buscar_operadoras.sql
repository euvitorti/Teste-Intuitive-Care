SELECT * FROM operadoras_ativas
WHERE razao_social ILIKE %s
LIMIT 10;