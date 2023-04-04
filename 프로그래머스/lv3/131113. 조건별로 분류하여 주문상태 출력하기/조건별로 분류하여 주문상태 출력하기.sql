-- 코드를 입력하세요
SELECT ORDER_ID, 
PRODUCT_ID, 
DATE_FORMAT(OUT_DATE, '%Y-%m-%d'), 
IF(OUT_DATE is null, '출고미정', IF(DATE_FORMAT(OUT_DATE, '%m-%d') <= '05-01', '출고완료','출고대기')) as '출고여부'
FROM FOOD_ORDER 
ORDER BY ORDER_ID