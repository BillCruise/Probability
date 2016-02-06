# Coin Flip Sequences
# When flipping a fair coin until either HTH or HTT is first reached,
# which sequence will take longer on average?

import random

def coin_flip_sequences():
    samples = 10000

    # HTH - Assume True = H
    total_flips = 0
    for i in range(samples):
        prev1 = None
        prev2 = None
        current = None
        flips = 0
        while True:
            prev1 = prev2
            prev2 = current
            current = random.random() < 0.5
            flips += 1
            if prev1 == True and prev2 == False and current == True:
                total_flips += flips
                break

    average = total_flips / samples
    print("Average number of flips before HHT:", average)

    # HTT - Assume True = H
    total_flips = 0
    for i in range(samples):
        flips = 0
        prev1 = None
        prev2 = None
        current = None
        while True:
            prev1 = prev2
            prev2 = current
            current = random.random() < 0.5
            flips += 1
            if prev1 == True and prev2 == False and current == False:
                total_flips += flips
                break

    average = total_flips / samples
    print("Average number of flips before HTT:", average)


if __name__ == '__main__':
    coin_flip_sequences()
