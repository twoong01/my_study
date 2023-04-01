-- 코드를 입력하세요
SELECT FI.FLAVOR
FROM FIRST_HALF as FI, ICECREAM_INFO as IC
WHERE FI.FLAVOR = IC.FLAVOR and FI.TOTAL_ORDER > 3000 and IC.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;