"""
Write a program which converts a number of seconds to the format 'hours: minutes: seconds'.
The program gets a number of seconds as input and prints the result on a screen.
You need to write your solution in the form of function(s) only. See the example below.

Example:

Input: 600

Output: '00:10:00'

"""
def helper(n):
    res = ""
    if n < 9:
        res = '0'+ str(n)
    else:
        res = str(n)
    return res
def convert_second(second):
    """
    1m = 60s
    1h = 3600s
    """
    h = 0
    m = 0
    s = 0
    while second != 0:
        if second > 3600:
            h = int(second/ 3600)
            second = second % 3600
        elif second > 60:
            m = int(second/ 60)
            second = second % 60
        else:
            s = second

    return helper(h) + ':' + helper(m)+':'+helper(s)

second = int(input())
res = convert_second(second)

print(res)
