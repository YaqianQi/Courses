s = input().split()
final = ''
lst = []
for x in s:
    if int(x) != 142:
        if int(x) % 2 == 0:
            lst.append(x)
    else:
        break
final = ' '.join(x for x in lst)
print(final)