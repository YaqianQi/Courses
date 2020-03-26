"""
Write a program which determines the quarter for the entered month.
The program gets a month number as input and prints it's quarter.
You need to write your solution in the form of function(s) only. See the example below.

Example

Input: 2

Output: 1

Hint! In this task we assume that quarters do not overlap with seasons, i.e.
for instance the first quarter includes 1st, 2nd and 3d months.
"""

def determine_quarter(month):
    if month % 3 == 0:
        return int(month / 3)
    else:
        return int(month/3) + 1
month = int(input())
quarter = determine_quarter(month)
print(quarter)
