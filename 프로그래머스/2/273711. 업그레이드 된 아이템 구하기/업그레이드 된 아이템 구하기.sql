-- 테이블: 아이템 정보, 아이템 관계
-- 아이템 희귀도가 RARE인 아이템의
-- 모든 다음 업그레이드 아이템
-- 아이템 아이디 내림차순
-- RARE인 아이템을 PARENT로 가지는 애들

-- 1. RARE인 아이템 필터링
-- 2. 조인

WITH CHILD_ITEM (ITEM_ID)
AS (SELECT T.ITEM_ID
    FROM ITEM_TREE T
    JOIN ITEM_INFO I ON T.PARENT_ITEM_ID = I.ITEM_ID
    WHERE I.RARITY = 'RARE')

SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM CHILD_ITEM C
JOIN ITEM_INFO I USING(ITEM_ID)
ORDER BY ITEM_ID DESC;