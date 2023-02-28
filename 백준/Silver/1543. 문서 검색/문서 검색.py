import re
note = input()
check = input()
cnt = 0
i = 0
while i <= len(note) - len(check):
    if note[i:i + len(check)] == check:
        cnt += 1
        i += len(check)
    else:
        i += 1
print(cnt)