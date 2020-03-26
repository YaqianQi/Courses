"""
Write a program which rearranges digits of a number which does not contain zeros in reverse order.
You are supposed to use recursion to solve this task.
The program gets a number which does not contain zeros as input.
Print the resulting number on a screen. See the example below.

Example:

Input: 1234

Output: 4321


prod = 0 + 4 * 10 = 40
rev (123, 40)

prod = 40 * 10 + 3 * 10 = 430
rev (12, 430)
prod = 430 * 10 + 2 * 10 = 4320
rev(1, 4320)
prod + 1
"""

def rev(x, prod=0):
    if x < 10:
        return prod + x
    else:
        prod = prod * 10 + x%10 * 10
        return rev(x // 10, prod)

n = int(input())
res = rev(n)
print(res)
