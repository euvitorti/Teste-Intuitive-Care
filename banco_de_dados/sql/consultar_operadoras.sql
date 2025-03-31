SELECT 
    data,
    reg_ans,
    vl_saldo_final
FROM demonstracoes_contabeis
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
  AND data BETWEEN %(data_inicio)s AND %(data_fim)s
ORDER BY vl_saldo_final DESC
LIMIT 10;
