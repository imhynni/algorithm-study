-- 2022년 5월에 예약한 환자 수
-- 진료과코드 별로 조회
-- '진료과 코드', '5월예약건수'
-- 진료과별 예약 환자 수 기준 오름차순, 그 다음은 진료과 코드 기준

-- 코드를 입력하세요
SELECT MCDP_CD AS '진료과 코드', COUNT(DISTINCT PT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
ORDER BY COUNT(DISTINCT PT_NO), MCDP_CD;