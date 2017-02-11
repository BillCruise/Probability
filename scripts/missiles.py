# Missiles
# If a certain missile will hit its target one out of four times,
# and four such missiles are fired at the same target, what is the
# probability that the target will be hit?

import random

def missiles():
    samples = 10000
    hits = 0

    for i in range(samples):
        hit = False
        for j in range(4):
            if random.random() < 0.25:
                hit = True
        if hit:
            hits += 1

    average = hits / samples
    print("Probability that the target will be hit:", average)

if __name__ == '__main__':
    missiles()
