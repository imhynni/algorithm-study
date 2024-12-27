-- 테이블: 잡은 물고기 정보, 물고기 이름 정보
-- 잡은 Bass, snapper 수

-- 물고기 종류 알아내고
-- 종류로 필터링, 카운트

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO I
JOIN (
    SELECT FISH_TYPE
    FROM FISH_NAME_INFO
    WHERE FISH_NAME IN ('bass', 'snapper')
) T ON I.FISH_TYPE = T.FISH_TYPE;