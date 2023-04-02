-- 코드를 입력하세요
SELECT count(USER_ID) as USERS
FROM USER_INFO
WHERE (AGE >= 20 and AGE <= 29) and year(joined) = '2021'