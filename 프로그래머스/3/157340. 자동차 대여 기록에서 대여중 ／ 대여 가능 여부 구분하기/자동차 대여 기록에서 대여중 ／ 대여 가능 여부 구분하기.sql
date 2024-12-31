-- 2022 10 16
-- 대여중, 대여가능 표시
-- 자동차 아이디 내림차순

-- 가능한 자동차만 필터링
-- 카 아이디 중복 제거해서 가능한 자동차에 속하는지 확인하며 분기

SELECT CAR_ID,
    IF(MAX('2022-10-16' BETWEEN START_DATE AND END_DATE) = 1,
       '대여중', '대여 가능') AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
