# The Little End of the Stick
# (a) if a stick is broken in two at random, what is the average length
# of the smaller piece?
# (b) (For calculus students.) What is the average ratio of the smaller
# length to the larger?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 42

import random

def little_end_of_the_stick():
    samples = 10000
    total_len = 0.0
    total_ratio = 0.0

    for i in range(samples):
        # assume a stick of unit length
        s1 = random.random()
        s2 = 1.0 - s1

        if s1 < s2:
            total_len += s1
            total_ratio += (s1 / s2)
        else:
            total_len += s2
            total_ratio += (s2 / s1)

    average_len = total_len / samples
    print("Average length of the smaller piece:", average_len)
    average_ratio = total_ratio / samples
    print("Average ratio of smaller to larger:", average_ratio)


if __name__ == '__main__':
    little_end_of_the_stick()
