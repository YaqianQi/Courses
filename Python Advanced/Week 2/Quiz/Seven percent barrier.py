"""
Party elections are held in one country. 
To reach the next stage of the election, the party must overcome the seven percent barrier of all votes.


INPUT
The first line of the input contains the word 'PARTIES:'. 
Then comes the list of parties participating in the elections. 
Then comes a line containing the word 'VOTES:'. It is followed by the names of the parties that voters voted for, one party per line. 
It is guaranteed that all vote lines are presented in the list of parties.

OUTPUT 
The program should print the names of the parties that received at least 7\%7% of the votes 
in the order in which they follow in the first list.

"""
read_mode = None
parties = []
votes = dict()

while True:
    input_line = input()
    if input_line == '':
        break

    if read_mode is None and input_line == 'PARTIES:':
        read_mode = 'PARTIES:'
        continue

    if input_line == 'VOTES:':
        read_mode = 'VOTES:'
        continue

    if read_mode == 'PARTIES:':
        parties.append(input_line)
        votes[input_line] = 0
    elif read_mode == 'VOTES:':
        votes[input_line] += 1

total_voices = sum(votes.values())
for party in parties:
    if votes[party] * 100 >= total_voices * 7:
        print(party)

