"""
Write a program which gets name, surname and age in a single string from as input and prints on a screen
 this information in the format 'Name: _____. Surname: ____. Age: __.'.
 You need to write your solution in the form of function(s) only. See the example below.

Example:

Input: 'Andrei Ivanchenko 15'

Output: 'Name: Andrei. Surname: Ivanchenko. Age: 15.'
"""

def name_printer(s):
    lst = s.split()
    name = lst[0]
    surname = lst[1]
    age = lst[2]
    print('Name: {}. Surname: {}. Age: {}.'.format(name, surname, age))
s = input()
name_printer(s)
