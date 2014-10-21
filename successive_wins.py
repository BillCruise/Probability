# Successive Wins
# To encourage Elmer's promising tennis career, his father offers him a
# prize if he wins (at least) two tennis sets in a row in a three-set
# series to be played with his father and the club champion alternately:
# father-champion-father or champion-father-champion, according to
# Elmer's choice. The champion is a better player than Elmer's father.
# Which series should Elmer choose?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 2

import random

def successive_wins():
    samples = 10000
    fcf_wins = 0
    cfc_wins = 0

    # assume Elmer has an 80% chance of winning against his father
    # and only a 40% chance of winning agains the club champion.

    for i in range(samples):
        # father-champion-father series
        set1 = random.random() < 0.8
        set2 = random.random() < 0.4
        set3 = random.random() < 0.8

        if (set1 and set2) or (set2 and set3):
            fcf_wins += 1

        # champion-father-champion series
        set1 = random.random() < 0.4
        set2 = random.random() < 0.8
        set3 = random.random() < 0.4

        if (set1 and set2) or (set2 and set3):
            cfc_wins += 1

    fcf_avg = fcf_wins / samples
    cfc_avg = cfc_wins / samples

    print("Elmer's win percent in father-champion-father series:", fcf_avg)
    print("Elmer's win percent in champion-father-champion series:", cfc_avg)



if __name__ == '__main__':
    successive_wins()
