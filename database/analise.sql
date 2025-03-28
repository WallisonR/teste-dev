-- Quais as 10 operadoras com maiores despesas no último trimestre?
SELECT op.operadora_id, op.nome_operadora, SUM(dc.valor) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN dados_cadastrais_op_ativas op ON dc.operadora_id = op.operadora_id
WHERE dc.categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
AND dc.data_evento >= CURRENT_DATE - INTERVAL '3 MONTH'
GROUP BY dc.operadora_id
ORDER BY total_despesas DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT op.operadora_id, op.nome_operadora, SUM(dc.valor) AS total_despesas
FROM demonstracoes_contabeis dc
JOIN dados_cadastrais_op_ativas op ON dc.operadora_id = op.operadora_id
WHERE dc.categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
AND dc.data_evento >= CURRENT_DATE - INTERVAL '1 YEAR'
GROUP BY dc.operadora_id
ORDER BY total_despesas DESC
LIMIT 10;
