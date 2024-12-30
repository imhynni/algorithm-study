-- 테이블: 자동차 정보, 대여 기록 정보, 할인 정책 정보
-- 세단, SUV 중에 2022.11.01-2022.11.30 대여 가능
-- 30일간 대여 금액 50만원 이상, 200만원 미만
-- 대여 금액 내림차순, 종류 오름차순, 아이디 내림차순

-- 자동차 정보, 대여 기록 조인 -> suv, 세단 필터링, 대여 기간 필터링
-- 정책에서 세단, suv, 30일 필터링
-- 요금, 할인율로 30일 금액 계산

WITH CARS AS (
    SELECT C.CAR_ID, CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR C
    WHERE CAR_TYPE IN ('세단', 'SUV')
        AND C.CAR_ID NOT IN (
            SELECT H.CAR_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
            WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
        )
),
CARS_FEE AS (
    SELECT C.CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100) AS FEE
    FROM CARS C
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE AND DURATION_TYPE = '30일 이상'
)

SELECT *
FROM CARS_FEE
WHERE 500000 <= FEE AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;