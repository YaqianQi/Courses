
s = input().split()
lst = s
for i in range(len(lst)):
    for j in range(i, len(lst)):
        if lst[j] > lst[i]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
final_res = ' '.join(x for x in lst)
print(final_res)
