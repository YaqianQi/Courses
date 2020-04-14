lst = []
s = ''
while True:
    text = input()
    if not text:
        break

    t = ' '.join(x for x in text.split())
    s += ' '+ t
lst = [x for x in s.split()]
res = ""
idx_dict = {}
idx = 0 
for i in range(len(lst)):
    res += str(idx_dict.get(lst[i], -1)) + " "
    idx_dict[lst[i]] = i
print(res)


"""
She sells sea shells on the sea shore;
-1   -1    -1 -1     -1 -1  2     -1 
            0               7
"""