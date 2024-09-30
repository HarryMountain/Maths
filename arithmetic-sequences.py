# importing itertools which is a library that allows you to get all the combinations of a list
import itertools
import numpy as np


# function taking sequence as input and returning whether sequence is arithmetic
def is_arithmetic(s):
    return np.all(np.diff(s, 2) == 0)  # checking for arithmetic


total = 0
# generating list of permutations of the list [0, 1,..., 8, 9] of range 10
perms = list(itertools.permutations(range(10), 10))

# taking each list of 10 numbers and splitting it into 5 groups of 2
for perm in perms:  # looping through each combination
    sequence = []
    for i in range(0, 9, 2):  # looping through the list to get the groups of two
        sequence.append(int(str(perm[i]) + str(perm[i+1])))  # concatenating the two numbers
    # checks to reduce search time -if not in ascending order it is not checked
    if [(sequence[k + 1] - sequence[k]) > 0 for k in range(len(sequence) - 1)].count(True) == len(sequence) - 1:  # checking for ascending order
        if is_arithmetic(sequence):
            total += sum(sequence)
            print(sequence)
print(total)
