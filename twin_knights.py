# Twin Knights
# (a) Suppose King Arthur holds a jousting tournament where the jousts are
# in pairs as in a tennis tournament. The 8 knights in the tournament are
# evenly matched, and they include the twin knights Balin and Balan.
# What is the chance that the twins meet in a match during the tournament?
# (b) Replace 8 by 2^n in the above problem. Now what is the chance they meet?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 17

import random

def twin_knights():
    samples = 10000
    total = 0

    for i in range(samples):
        ladder = [x for x in range(8)]
        random.shuffle(ladder)
        if twins_meet(ladder):
            total += 1

    average = total / samples
    print("Chance that the twins meet in a match:", average)


# Check to see if the "twins" (0 and 1) meet 
# in a given shuffled tournament ladder.
def twins_meet(ladder):
    if(len(ladder) == 2):
        if all(x < 2 for x in ladder):
            return True
        else:
            return False
    else:
        next_round_ladder = []
        for j, k in zip(ladder[0::2], ladder[1::2]):
            if j < 2 and k < 2:
                return True
            winner = j if (random.random() < 0.5) else k
            next_round_ladder.append(winner)
        return twins_meet(next_round_ladder)


if __name__ == '__main__':
    twin_knights()
