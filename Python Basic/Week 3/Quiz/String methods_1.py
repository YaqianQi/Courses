s = input()
line1 = s[0]
line2 = s[1:5]
line3 = s[::-1]
line4 = ""
for i in range(2,len(s),3):
    line4 += s[i]
print(line1)
print(line2)
print(line3)
print(line4)