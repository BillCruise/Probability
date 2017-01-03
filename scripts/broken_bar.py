# The Broken Bar
# A bar is broken at random in two places. Find the average size of the
# smallest, the middle-sized, and the largest pieces.
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 43

import random

def broken_bar():
    samples = 10000
    shortest = 0.0
    middle = 0.0
    longest = 0.0

    for i in range(samples):
        # simulate breaking the bar in two spots
        breaks = []
        breaks.append(random.random())
        breaks.append(random.random())
        breaks.sort()

        # find the lengths of the pieces
        pieces = []
        pieces.append(breaks[0])
        pieces.append(breaks[1] - breaks[0])
        pieces.append(1.0 - breaks[1])

        pieces.sort()
        shortest += pieces[0]
        middle += pieces[1]
        longest += pieces[2]

    print("Average length of the smallest piece:", shortest / samples)
    print("Average length of the middle piece:", middle / samples)
    print("Average length of the largest piece:", longest / samples)



if __name__ == '__main__':
    broken_bar()
