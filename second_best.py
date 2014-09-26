# Will Second-Best Be Runner-Up?
# A tennis tournament has 8 players. The number a player draws from a
# hat decides his first-round run in the tournament ladder.
# Suppose that the best player always defeats the next best and that
# the latter always defeats all the rest. The loser of the finals gets
# the runner-up cup. What is the chance that the second-best player
# wins the runner-up cup?
#
# From: Fifty Challenging Problems in Probability
#       by Frederic Mosteller
#       Problem 16

import random

def second_best():
    samples = 10000
    total = 0

    for i in range(samples):
        ladder = [x for x in range(8)]
        random.shuffle(ladder)

        second_place = runner_up(ladder)
        if(second_place == 1):
            total += 1

    average = total / samples
    print("Chance that the second-best player wins the runner-up cup:", average)

# find out which player was the runner-up in the given ladder arrangement
def runner_up(ladder):
    if(len(ladder) == 2):
        return max(ladder)
    else:
        next_round_ladder = []
        for j, k in zip(ladder[0::2], ladder[1::2]):
            next_round_ladder.append(min(j, k))
        return runner_up(next_round_ladder)
    
    
if __name__ == '__main__':
    second_best()
    
