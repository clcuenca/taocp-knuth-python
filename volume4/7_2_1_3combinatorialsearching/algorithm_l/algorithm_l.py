# General Algorithms - Combinatronics
# Lexicographic Combination Generator
# From Knuth's The Art of Computer Programming
# Author: Carlos L. Cuenca
# Date: 10/21/20

# -------
# Imports

import sys

# -------
# Program

for line in sys.stdin:

	currentLine = line.strip().split(" ")
	array = [int(number) for number in currentLine]
	
	# As an example, we go through each n choose t
	for t in range(1, len(array)):

		combinations = [0]*(t+2)

		# Clear the combinations array
		for j in range(t):
			combinations[j] = j

		# Assign the sentinels
		combinations[t] = len(array)
		combinations[t + 1] = 0

		j = 0

		while j < t:

			# Visit the combination. In this case we print the indices
			combinationString = ""

			for index in range(t):

				combinationString += str(combinations[index]) + " "

			print(combinationString)

			# Find J
			j = 0

			while(combinations[j] + 1 == combinations[j + 1]):

				combinations[j] = j

				j += 1

			combinations[j] += 1	

