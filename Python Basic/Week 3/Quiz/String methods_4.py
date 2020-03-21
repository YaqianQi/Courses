s = input()
result = ''.join([i for i in s if not i.isdigit()])
print(result)