# Hit and Run
# A cab was involved in a hit and run accident at night. Two cab companies,
# the Green and the Blue, operate in the city.
# You are given the following data:
# (a) 85% of the cabs in the city are Green and 15% are Blue.
# (b) A witness identified the cab as Blue. The court tested the reliability
#     of the witness under the same circumstances that existed on the night
#     of the accident and concluded that the witness correctly identified
#     each one of the two colors 80% of the time and failed 20% of the time.
# What is the probability that the cab involved in the accident was
# Blue rather than Green?
#
# From: Randomness
#       by Deborah J. Bennett
#       page 2

import random

def hit_and_run():
    samples = 10000
    id_blue = 0
    both_blue = 0

    for i in range(samples):
        cab_blue = (random.random() < 0.15)
        witness_correct = (random.random() < 0.80)

        if cab_blue and witness_correct:
            both_blue += 1
            id_blue += 1
            
        if (not cab_blue) and (not witness_correct):
            id_blue += 1

    average = both_blue / id_blue
    print("Probability that the cab was Blue:", average)


if __name__ == '__main__':
    hit_and_run()
