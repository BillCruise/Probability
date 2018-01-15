# Bold Play vs. Cautious Play
# At Las Vegas, a man with $20 needs $40, but he is too embarrassed to
# wire his wife for more money. He decides to invest in roulette (which
# he doesn't enjoy playing) and is considering two strategies: bet the
# $20 on "evens" all at once and quit if he wins or loses, or bet on
# "evens" one dollar at a time until he has won or lost $20.
# Compare the merits of the strategies.
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 37

import random

def bold_play_vs_cautious_play():
    samples = 10000
    wins = 0

    for i in range(samples):
        bank = 20
        while bank > 0 and bank < 40:
            spin = random.randint(0, 37)
            if spin > 0 and (spin % 2 == 0):
                bank += 1
            else:
                bank -= 1
        if bank == 40:
            wins += 1

    average = wins / samples
    print("Odds of winning $20, $1 at a time at roulette:", average)
        

    
if __name__ == '__main__':
    bold_play_vs_cautious_play()
