-- 테이블: 플밍 언어 정보, 스킬 정보
-- python, c# 스킬 가진 개발자 정보 조회
-- 아이디 오름차순

SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S ON S.NAME IN ('Python', 'C#') AND D.SKILL_CODE & S.CODE = S.CODE
ORDER BY ID;