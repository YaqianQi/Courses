"""
After a lengthy meeting, the company's director decided to order a taxi to take the staff home. 
He ordered NN cars -− exactly as many employees as he had.
However, when taxi drivers arrived, it turned out that each taxi driver has a different fare for 11 kilometer.

The director knows the distance from work to home for each employee (unfortunately, all employees live in different directions, 
so it is impossible to send two employees in one car). Now the director wants to find out how much to pay for a taxi for all employees. 
Obviously, the director wants to pay as little as possible.

Input data:
10 20 30
50 20 30

Program output:
1700


"""

dist_list = sorted([int(x) for x in input().split()])
rates_list = sorted([int(x) for x in input().split()],reverse = True)
##import numpy as np
#res = np.dot(dist_list , rates_list)
res = 0
for i in range(len(dist_list)):
    res += dist_list[i] * rates_list[i]
print(res)

