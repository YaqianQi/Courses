"""
The shoe store sells shoes of different sizes. It is known that one pair of shoes can be put on another if it is at least three sizes larger. 
A customer came to the store. Need to find how many pairs of shoes can offer him the seller so that customer can put them all on at the same time.

Input format: The first number is the size of the customer's foot (he will not be able to put on a smaller shoe), in the next line - 
the size of each pair of shoes in the store through a space.

Output format: Print one number - the maximum number of pairs of shoes that the customer can wear at the same time.

Input data:
26 
30 35 40 41 42

Program output:
3
"""

customer_leg_size = int(input())
shop_shoe_sorted_sizes = sorted([int(size) for size in input().split()])

n_suitable_pairs = 0
prev_suitable_size = customer_leg_size - 3

for shoe_size in shop_shoe_sorted_sizes:
    if shoe_size >= prev_suitable_size + 3:
        prev_suitable_size = shoe_size
        n_suitable_pairs += 1

print(n_suitable_pairs)