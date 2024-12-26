-- 테이블: 식당 정보, 리뷰 정보
-- 서울 위치
-- 리뷰 평균점수 소수점 세번째에서 반올림
-- 평균점수 내림차순, 즐겨찾기 수 내림차순

-- 1. 서울 필터링
-- 2. 식당별로 리뷰 평균 점수 산출

SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, ROUND(AVG(r.review_score), 2) AS SCORE
FROM (SELECT * FROM rest_info WHERE ADDRESS LIKE '서울%') AS i
JOIN rest_review r USING(rest_id)
GROUP BY rest_id
ORDER BY score DESC, i.favorites DESC;