a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

set1 = set(a)
set2 = set(b)
lst = list(tuple(set1.intersection(set2)))
res = ' '.join(str(x) for x in lst)
print(res)
