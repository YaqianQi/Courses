s = input().split()
final = ''
lst = []
for x in s:
    if int(x) < 10:
        lst.append(x)
final = ' '.join(x for x in lst)
print(final)