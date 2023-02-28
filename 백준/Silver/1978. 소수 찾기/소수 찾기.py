n = int(input())
num_list = list((map(int, input().split())))
not_prime = list()
for i in num_list:
    if i == 1:
        not_prime.append(i)
    else:
        pow_i = pow(i, 2)
        for j in range(2, pow_i + 1):
            if i % j == 0 and i != j:
                not_prime.append(i)
                break
answer = len(num_list) - len(not_prime)
print(answer)