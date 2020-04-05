s = ''
while True:
    text = input()
    if not text:
        break

    t = ' '.join(x for x in text.split())
    s += ' '+ t
res = {}
final = []
for x in s.split():
    if x in res:
        res[x] += 1
    else:
        res[x] = 0
    final.append(res[x])

print(*final, sep = " ")

