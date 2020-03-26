"""
Write a program that takes a list of numbers as input and prints on a screen the sum of numbers in it.
The program gets a sequence of numbers separated by spaces as input.
You need to write your solution in the form of function(s) only. See the example below.

Example

Input: 1 2 3 4 5

Output: 15
"""

def get_sum(lst):
    return sum(lst)

lst = [int(x) for x in input().split()]
res = get_sum(lst)
print(res)
