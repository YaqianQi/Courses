"""
Write a program which determines whether a number is prime.
The program gets a number as input and prints 'YES'
if the number is prime, or 'NO' otherwise.
You need to write your solution in the form of function(s) only.
See the example below.

Examples

Test 1

Input: 3

Output: YES

Test 2

Input: 6

Output: NO
"""

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    else:
        return False
        

num = int(input())
if isPrime(num):
    print('YES')
else:
    print('NO')
