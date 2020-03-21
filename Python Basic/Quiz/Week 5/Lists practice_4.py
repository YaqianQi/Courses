s = input().split()
max_value = -2 ** 31
for x in s:
    if int(x) > max_value:
        max_value = int(x)
print(max_value)