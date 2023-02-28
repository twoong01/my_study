N = int(input())
rope = []
weight = []
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for i in range(N):
    weight.append(rope[i]*(i+1))
print(max(weight))