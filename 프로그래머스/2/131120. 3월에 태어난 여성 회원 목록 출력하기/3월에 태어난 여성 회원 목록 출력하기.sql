-- 생일 3월인 여성
-- 전화번호 Null 제외
-- 회원ID 오름차순

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(date_of_birth, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM member_profile
WHERE MONTH(date_of_birth) = 3 AND GENDER = 'W' AND TLNO IS NOT NULL
ORDER BY member_id;