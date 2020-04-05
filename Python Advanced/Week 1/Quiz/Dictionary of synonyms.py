#from collections import defaultdict
#import string
n = int(input())
name = {}
for _ in range(n):
    s = [x for x in input().split()]

    name[s[1]] = s[0]
    name[s[0]] = s[1]
query = input()
print(name[query])
#print(name)