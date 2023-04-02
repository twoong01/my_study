-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE, sum(f.total_order) as TOTAL_ORDER
FROM FIRST_HALF f
JOIN ICECREAM_INFO i
ON f.flavor = i.flavor
GROUP BY i.ingredient_type
ORDER BY TOTAL_ORDER;