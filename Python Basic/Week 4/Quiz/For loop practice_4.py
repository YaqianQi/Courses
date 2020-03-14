
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
if len(a)!=0 and len(b)!= 0:
    set1 = set(a)
    set2 = set(b)
    lst = tuple(set1.intersection(set2))
    print(lst)
else:
    print(tuple())
