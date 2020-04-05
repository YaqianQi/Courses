n_students = int(input())
all_languages = set()

for _ in range(n_students):
    n_languages = int(input())
    temp_languages_set = {input() for _ in range(n_languages)}
    all_languages |= temp_languages_set

print(len(all_languages))
print(*sorted(all_languages), sep='\n')

