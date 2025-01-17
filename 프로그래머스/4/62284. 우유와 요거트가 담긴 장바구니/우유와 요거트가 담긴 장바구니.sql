-- 장바구니 상품 정보
-- 우유, 요거트 동시 구입
-- 아이디 순
-- 우유 담은 장바구니, 요거트 담은 장바구니, 교집합

SELECT DISTINCT CART_ID
FROM (
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Milk'
) M
WHERE CART_ID IN (
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Yogurt'
)
ORDER BY CART_ID;