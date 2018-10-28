# Chances of dying
# Given 19 6-sided dice, what are the chances of rolling a sum of 57 or greater?

import random

def chance_of_dying():
    samples = 10000
    dice = 19
    sides = 6
    threshhold = dice * (sides / 2)

    exceeds_or_meets = 0
    for i in range(samples):
        total = 0
        for j in range(dice):
            total += random.randint(1, 6)
        if total >= threshhold:
            exceeds_or_meets += 1

    chances = exceeds_or_meets / samples
    print("Chance of dying:", chances)

if __name__ == '__main__':
    chance_of_dying()
