n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = n - 1
min_value = float('inf')
min_start = liquid[start]
min_end = liquid[end]
while start < end:
    value = (liquid[start] + liquid[end])
    if abs(value) < abs(min_value):
        min_value = value
        min_start = liquid[start]
        min_end = liquid[end]
    if value > 0:
        end -= 1
    else:
        start += 1
print(min_start, min_end)