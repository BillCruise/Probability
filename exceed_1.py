# Exceed 1
# Choose a random number between 0 and 1 and record its value.
# Do this again and add the second number to the first number.
# Keep doing this until the sum of the numbers exceeds 1.
# What's the expected value of the number of random numbers
# needed to accomplish this?

# http://math.stackexchange.com/questions/111314/choose-a-random-number-between-0-and-1-and-record-its-value-keep-doing-it-until

import random

def exceed_1():
    samples = 100000
    total = 0

    for i in range(samples):
        draws = 0
        draw_sum = 0.0
        while draw_sum <= 1.0:
            draw_sum += random.random()
            draws += 1
        total += draws

    average = total / samples
    print("Expected number of draws to exceed 1:", average)

if __name__ == '__main__':
    exceed_1()
