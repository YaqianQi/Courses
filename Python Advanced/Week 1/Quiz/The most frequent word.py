s = ''
while True:
    text = input()
    if not text:
        break

    t = ' '.join(x for x in text.split())
    s += ' '+ t
import collections
c = collections.Counter()
for x in s.split():
    c[x] += 1
freq = max([x for x in c.values()])
res = []
for k, v in c.items():
    if v == freq:
        res.append(k)
res = sorted(res)
print(res[0])