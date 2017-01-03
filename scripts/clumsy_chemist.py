# The Clumsy Chemist
# In a laboratory, each of a handful of thin 9-inch glass rods had one tip
# marked with a blue dot and the other with a red. When the laboratory
# assistant tripped and dropped them onto the concrete floor, many broke
# into three pieces. For these, what was the average length of the
# fragment with the blue dot?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 39

import random

def clumsy_chemist():
    samples = 10000
    total = 0.0

    for i in range(samples):
        break1 = random.random()
        break2 = random.random()

        blue = break1 if (break1 < break2) else break2
        total += blue

    average = (total / samples) * 9
    print("Average length of fragment with blue dot:", average)


if __name__ == '__main__':
    clumsy_chemist()
