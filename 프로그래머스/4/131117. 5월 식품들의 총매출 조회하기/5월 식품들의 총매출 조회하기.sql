-- 생산일자 2022.05
-- 식품 ID, 식품 이름, 총매출
-- 총매출 내림차순, 식품 ID 오름차순
-- 1. 생산일자 필터링
-- 2. 조인해서 가격 알아내고 아이디로 그룹핑해서 총매출 구하기
-- 3. 아이디로 조인해서 식품 이름 가져오기
-- 4. 정렬

SELECT O.PRODUCT_ID, P.PRODUCT_NAME, SUM(O.AMOUNT * P.PRICE) AS TOTAL_SALES
FROM FOOD_ORDER O
JOIN FOOD_PRODUCT P
ON O.PRODUCT_ID = P.PRODUCT_ID
WHERE O.PRODUCE_DATE >= '2022-05-01' AND O.PRODUCE_DATE < '2022-06-01'
GROUP BY O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC;