# Section 1.1 - Algorithm E
# From Knuth's The Art of Computer Programming
# Author: Carlos L. Cuenca
# Date: 10/21/20

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def algorithm_e(m, n):

    m = abs(m)
    n = abs(n)

    if m < n:

        temp = n
        n = m
        m = temp

    remainder = m % n

    while remainder > 0:

        remainder = m % n

        if remainder == 0: break

        m = n
        n = remainder

    return n

# -------
# Program

for line in sys.stdin:

    stripped = line.strip().split(" ")

    array = [int(number) for number in stripped]

    print(str(algorithm_e(array[0], array[1])))