-- 이름에 el
-- 아이디와 이름 조회, 이름순 
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'DOG' AND NAME LIKE '%el%'
ORDER BY NAME;