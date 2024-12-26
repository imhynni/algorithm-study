-- 상반기 주문정보 테이블, 성분 정보 테이블
-- 총 주문량이 3000보다 높고
-- 주성분이 과일인 아이스크림의 맛
-- 총주문 큰 순서대로

-- 1. 주문량 3000보다 높은 거 필터링
-- 2. flavor로 조인하고 과일 성분인 거 필터링
-- 3. 맛 조회, 주문량 내림차순

SELECT II.flavor
FROM first_half FH
JOIN icecream_info II ON FH.flavor = II.flavor
WHERE FH.total_order > 3000 AND II.ingredient_type = 'fruit_based'
ORDER BY FH.total_order desc;