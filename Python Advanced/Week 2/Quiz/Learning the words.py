"""
Peter wants to learn new English words, but wants to do it in a certain sequence. 
First he chooses short words, and if the words are the same length he chooses in lexicographical order when reading from right to left.
 Help Peter to put the order of words from the given list.

Input data:
3
news
are
taxi

Program output:
are
taxi
news
"""

n_words = int(input())
words = [input() for _ in range(n_words)]
# sprt based on word length and lexicographical order from right to left 
words.sort(key=lambda word: (len(word), word[::-1]))
print(*words, sep='\n')