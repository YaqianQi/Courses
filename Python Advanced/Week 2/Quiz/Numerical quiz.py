"""
Input data:
4
7092
6558
1744
498

Comparison values:
7092 -> (7 - 2) + (0 - 9) = -4
6558 -> (6 - 8) + (5 - 5) = -2
1744 -> (1 - 4) + (7 - 4) = 0
498 -> (4 - 8) = -4

Program output:
498
7092
6558
1744
"""

def calc_cmp_value(number):
    s = str(number)
    cmp_value = 0
    
    for i in range(len(s) // 2):
        cmp_value += int(s[i]) - int(s[-i - 1])
    return cmp_value

n_numbers = int(input())
numbers = [int(input()) for _ in range(n_numbers)]
# sort based on vaule customized function and value 
numbers.sort(key=lambda number: (calc_cmp_value(number), number))
print(*numbers, sep='\n')