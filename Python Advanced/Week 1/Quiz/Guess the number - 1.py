
"""

August and Beatrice are playing a game. August thought a natural number from 11 to NN. Beatrice tries to guess this number,
 for this she calls some sets of natural numbers. August answers Beatrice YES if the conceived number is in her named set or NONO otherwise.
 After several questions, Beatrice is confused about what questions she asked and what answers she received and asks you to help her determine what numbers August might have conceived.

Input format: The first line of input data contains the number NN — the largest number that August could guess.
Then there are lines containing Beatrice's questions. Each line is a set of numbers separated by spaces.
Each line with the question is followed by August's answer: YES or NO. Finally, the last line of input contains one word HELPHELP.

Output format: Print all the numbers that August could have conceived (separated by a space, in ascending order).

Input data:
10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP

Program output:
1 3 5

"""
n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    numbers_or_help = input()
    if numbers_or_help == 'HELP':
        break

    question_numbers_set = {int(x) for x in numbers_or_help.split()}
    answer = input()

    if answer == 'YES':
        possible_numbers &= question_numbers_set
    else:
        possible_numbers -= question_numbers_set

print(*sorted(possible_numbers))