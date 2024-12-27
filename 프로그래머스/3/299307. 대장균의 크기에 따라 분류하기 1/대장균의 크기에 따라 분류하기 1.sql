-- 테이블: 대장균 정보
-- 크기가 100 이하: low, 100 초과 1000 이하: medium, 1000 초과 high
-- 아이디 오름차순

SELECT
    ID,
    (CASE
        WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
        WHEN SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END) AS SIZE
FROM ECOLI_DATA
ORDER BY ID;
