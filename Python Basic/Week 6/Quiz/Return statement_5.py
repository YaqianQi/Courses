"""
Write a program which returns the area and the perimeter of a rectangle.
The program gets lengths of two sides as one string with two numbers separated by space.
You need to write your solution in the form of function(s) only. The output format is as in the example below.

Example

Input: 1 2

Output:

Area: 2

Perimeter: 6
"""

def cal_area_perimeter(l, w):
    area = l * w
    perimeter = 2 * (l + w)
    return area, perimeter

lst = input().split()
l = int(lst[0])
w = int(lst[1])
area, perimeter = cal_area_perimeter(l, w)
print('Area: {}'.format(area))
print('Perimeter: {}'.format(perimeter))
