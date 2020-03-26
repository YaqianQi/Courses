"""
Write a program which calculates the sum of digits of any natural number and prints it on a screen.
You are supposed to use recursion to solve this task. The program gets a natural number as input.
See the example below.

Example:

Input: 123

Output: 6
"""

def sum_of_digit1(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res

def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))

n = int(input())
res = sum_of_digit(n)
print(res)
