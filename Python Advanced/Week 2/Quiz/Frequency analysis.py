"""
The text is given. Print all unique words found in the text, one for each line.
Words should be sorted by their frequency in the text, and in the lexicographical order,
if they appear at the same frequency.

Input data:
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme


Program output:
damme
is
name
van
bond
claude
hi
my
james
jean
what
your
"""

word_count_dict = dict()

while True:
    input_line = input()
    if input_line == '':
        break

    for word in input_line.split():
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

word_count_list = list(word_count_dict.items())
# sorted by their frequency in the text, and in the lexicographical order
word_count_list.sort(key=lambda x: (-x[1], x[0]))
for word, cnt in word_count_list:
    print(word)

