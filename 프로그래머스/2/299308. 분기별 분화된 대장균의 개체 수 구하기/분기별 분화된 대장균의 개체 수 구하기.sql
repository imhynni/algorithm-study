SELECT CONCAT(QUARTER(differentiation_date), 'Q') AS QUARTER, COUNT(*) AS ECOLI_COUNT
FROM ecoli_data
GROUP BY CONCAT(QUARTER(differentiation_date), 'Q')
ORDER BY QUARTER;
