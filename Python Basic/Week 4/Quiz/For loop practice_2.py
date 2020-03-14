start = int(input())
end = int(input())+1
res = ' '.join(str(x) for x in range(start, end) if x % 2 == 0)
print(res)
