"""
The input line contains a sequence of numbers separated by a space.
For each number print the word YESYES (on a separate line) if this number was previously encountered in the sequence, or NO if it was not.

Input format: A list of numbers written on one line.

Output format: Print the answer to the task.


"""

numbers = [int(x) for x in input().split()]
unique_elements_set = set()

answers = []
for number in numbers:
    if number in unique_elements_set:
        answers.append('YES')
    else:
        answers.append('NO')
        unique_elements_set.add(number)

print(*answers, sep='\n')