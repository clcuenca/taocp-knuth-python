# Section 1.1 - Algorithm F
# From Knuth's The Art of Computer Programming
# Author: Carlos L. Cuenca
# Date: 10/21/20

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def algorithm_f(m, n):
    
    m = abs(m);
    n = abs(n);

    if(m < n):

        temp = n
        n = m
        m = temp

    if n == 0: return m;

    return algorithm_f(n, m % n);


# -------
# Program

for line in sys.stdin:

    stripped = line.strip().split(" ")

    array = [int(number) for number in stripped]

    print(str(algorithm_f(array[0], array[1])))
