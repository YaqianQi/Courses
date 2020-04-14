"""
Database of sales of some online shop is given. Each line of the input file is a record of the following view: 
(customer item quantity), customer and item are strings without spaces.

Create a list of all customers, and for each customer, calculate the number of units of each item type.



Input data:
Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5


Program output:
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5
"""

guidebook = dict()

while True:
    input_line = input()
    if input_line == '':
        break

    name, product, count = input_line.split()
    count = int(count)

    if name not in guidebook:
        guidebook[name] = dict()
    guidebook[name][product] = guidebook[name].get(product, 0) + count

for name in sorted(guidebook.keys()):
    print(f'{name}:')
    for product in sorted(guidebook[name].keys()):
        print(f'{product} {guidebook[name][product]}')