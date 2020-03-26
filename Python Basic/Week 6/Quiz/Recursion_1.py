"""
Write a program which calculates the factorial of a number and prints it on a screen.
Keep in mind that you are supposed to use recursion to solve this task.
The program gets an integer number as input. See the example below.

Example:

Input: 5

Output: 120

Hint! Analyze the code which you wrote to solve the same task in the fourth week.
Compare these two solutions in terms of code parsimony and execution time.
What do you think, which solution is more effective according to that criteria?

The second one faster. For recursion, there should be n-1 stack memory to store the temporary value.
"""
#import time
#
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fact(n-1) * n
n = int(input())
res = fact(n)
print(res)
#print(time.time() - t)

"""t2 = time.time()
def fact2(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
res = fact2(n)
print(res)
print(time.time() - t2)"""
