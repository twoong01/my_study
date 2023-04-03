-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, sum(b.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_USER u
ON b.WRITER_ID = u.USER_ID
WHERE b.STATUS = 'DONE'
GROUP BY u.USER_ID
HAVING sum(b.PRICE) >= 700000
ORDER BY TOTAL_SALES