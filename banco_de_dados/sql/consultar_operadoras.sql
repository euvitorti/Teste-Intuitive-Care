SELECT
  d.reg_ans,
  o.nome_fantasia,
  SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o
  ON d.reg_ans = o.registro_ans
WHERE
  d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
  AND d.data BETWEEN %(data_inicio)s AND %(data_fim)s
GROUP BY
  d.reg_ans,
  o.nome_fantasia
ORDER BY
  total_despesas DESC
LIMIT 10;