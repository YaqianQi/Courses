n = int(input())
countries = {}
for _ in range(n):
    s = [i for i in input().split()]
    if s[0] not in countries:
        countries[s[0]] = []
        countries[s[0]] =  s[1:]
    else:
        countries[s[0]] = countries[s[0]].append(s[1:])

m = int(input())
res = []
for _ in range(m):
    city = input()
    for k, v in countries.items():
        if city in v:
           res.append(k)
print(*res, sep = "\n")
