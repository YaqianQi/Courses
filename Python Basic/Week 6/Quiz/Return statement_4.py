"""
Write a program which takes as input two strings and returns a single string
with sorted elements of the two strings in ascending order.
The program gets two strings separately as input and prints the resulting string.
You need to write your solution in the form of function(s) only. See the example below.

Example

Input:

987654321

GgfFEedDCcbBaA

Output:

123456789ABCDEFGabcdefg
"""

def merge_sort_two_string(s1,s2):
    s = sorted(s1+s2)
    return ''.join(x for x in s)

s1 = input()
s2 = input()

res = merge_sort_two_string(s1,s2)
print(res)
