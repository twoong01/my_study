-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID , TITLE, PRICE, 
if(status = 'DONE', '거래완료', if(status = 'RESERVED', '예약중', '판매중')) as STATUS
FROM used_goods_board
WHERE DATE_FORMAT(created_date, '%Y-%m-%d') = '2022-10-05'
ORDER BY board_id DESC;


# SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
#     (CASE WHEN STATUS = 'SALE' THEN '판매중'
#           WHEN STATUS = 'RESERVED' THEN '예약중'
#           WHEN STATUS = 'DONE' THEN '거래완료'
#     END) AS STATUS
# FROM USED_GOODS_BOARD
# WHERE DATE_FORMAT(CREATED_DATE,'%Y-%m-%d') = '2022-10-05'
# ORDER BY BOARD_ID DESC