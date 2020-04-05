
"""
August and Beatrice keep playing the game, but August started cheating. For each Beatrice's question, he chooses the answer YESYES or NONO, so that the set of possible conceived numbers remains as large as possible. For example, if August has a numbers between 11 and 55, and Beatrice asked about numbers 11 and 33, then August answers NONO, and if Beatrice asked about 1, 3, 41,3,4, then August answers YESYES. But if Beatrice mentions exactly half of the remaining numbers in her question, then August always answers NONO. August at the answer considers all previous questions of Beatrice and the answers to them, that is set of possible conceived numbers decreases.

Input format: The sequence of Beatrice's questions is given. The first line of input data contains the number NN -− the largest number that August could guess. Next come the lines containing Beatrice's questions. Each line is a set of numbers separated by spaces. The last line of input contains one word HELPHELP.

Output format: For each question of Beatrice, print August's answer to that question. Then print (through a space, in ascending order) all the numbers that August might have thought of after answering all Beatrice's questions.

Input data:
10
1 2 3 4 5
2 4 6 8 10
HELP

Program output:
NO
YES
6 8 10


"""
n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    numbers_or_help = input()
    if numbers_or_help == 'HELP':
        break

    question_numbers_set = {int(x) for x in numbers_or_help.split()}
    question_numbers_set &= possible_numbers

    if len(question_numbers_set) <= len(possible_numbers) // 2:
        possible_numbers -= question_numbers_set
        print('NO')
    else:
        possible_numbers &= question_numbers_set
        print('YES')

print(*sorted(possible_numbers))