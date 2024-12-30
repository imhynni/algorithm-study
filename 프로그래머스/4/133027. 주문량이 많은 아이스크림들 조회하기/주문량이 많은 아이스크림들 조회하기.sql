-- 테이블: 상반기 주문 정보, 7월 주문 정보
-- 7월 아이스크림 총 주문량 + 상반기 아이스크림 총 주문량
-- 큰 순서 상위 3개의 맛

-- 맛별로 총 주문량 구하기
-- 정렬하고 3개까지 조회

SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN JULY J USING(FLAVOR)
GROUP BY FLAVOR
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3;