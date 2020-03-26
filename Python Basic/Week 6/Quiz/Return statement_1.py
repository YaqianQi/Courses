
"""
Write a function which performs operations of a simple calculator.
The program gets the first number, the second number and the mathematical operator (+, -, * or /) one by one separately.
Then the program prints on a screen the result. See the example below.

Example:

Input:

1

2

+

Output:

3.0
"""
def simple_calculator(num1, num2,operator):
    res = 0
    if operator == '+' :
        res = num2 + num1
    elif operator == '-':
        res = num1 - num2
    elif operator == '*':
        res = num1 * num2
    elif operator == '/':
        res = num1 / num2
    return res
num1 = float(input())
num2 = float(input())
operator = input()
# +, -, * or /
res = simple_calculator(num1, num2,operator)
print(res)
