from collections import defaultdict
def check_upper(s):
    count = 0
    for x in s:
        if x.isupper():
            count += 1
    return count

n = int(input())
s = defaultdict(list)
for _ in range(n):
    word = input()
    s[word.lower()].append(word)

check = [x for x in input().split()]
cnt = 0
for x in check:
    if x.lower() in s:
        if x not in s[x.lower()] or check_upper(x) == 0 :
            cnt+= 1
    else:
        if check_upper(x)!= 1:
            cnt += 1
print(cnt)

