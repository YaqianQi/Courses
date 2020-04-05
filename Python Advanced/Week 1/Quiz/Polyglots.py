n_students = int(input())
everyone_known_languages = None

for _ in range(n_students):
    n_languages = int(input())
    temp_languages_set = {input() for _ in range(n_languages)}

    if everyone_known_languages is None:
        everyone_known_languages = temp_languages_set

    everyone_known_languages &= temp_languages_set

print(len(everyone_known_languages))
print(*sorted(everyone_known_languages), sep='\n')

