a = int(input())
b = int(input())
b_1 = b%10
b = b // 10
b_2 = b%10
b = b // 10

result_1 = a * (b_1)
result_2 = a * (b_2)
result_3 = a * (b)
result_4 = result_1 + result_2*10 + result_3*100
print(result_1)
print(result_2)
print(result_3)
print(result_4)