-- SUV
-- 평균 일일 대여 요금
-- 첫째자리 반올림

SELECT ROUND(AVG(daily_fee)) AS AVERAGE_FEE
FROM car_rental_company_car
WHERE car_type = 'SUV';