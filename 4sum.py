import numpy as np
from itertools import combinations, product
from collections import defaultdict

def sum4(data):
    # store 2-sums
    sum_of_2 = defaultdict(list)
    for i, j in combinations(range(len(data)), 2):
        k = data[i] + data[j]
        sum_of_2[k].append((i, j))

    # match pairs of 2-sums
    sum_of_4 = set()
    for k in sum_of_2:
    	# check if zero sum is even possible with the remaining numbers and current sum
        if k >= 0 and -k in sum_of_2: 
        	# if yes, then find all such combinations of 2-sums that add to zero
            for i, j in product(sum_of_2[k], sum_of_2[-k]):
                index = tuple(sorted(set(i + j)))
                # length of set might become 3 if there is common element in the 2-sum pairs
                if len(index) == 4:
                    sum_of_4.add(index)

    return sum_of_4

if __name__=='__main__':
	n = 10
	data = np.random.randint(-n, n, n)
	
	for index in sum4(data):
	    print(index, data[list(index)])

