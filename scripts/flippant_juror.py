# The Flippant Juror
# A three-man jury has two members each of whom independently has
# probability p of making the correct decision and a third member
# who flips a coin for each decision (majority rules). A one-man
# jury has probability p of mking the correct decision. Which jury
# has the better probability of making the correct decision?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 3

import random

def flippant_juror():
    samples = 10000
    correct = 0

    for i in range(samples):
        juror1 = random.random() < 0.8
        juror2 = random.random() < 0.8
        juror3 = random.random() < 0.5

        # check to see if two out of three jurors came
        # up with the "correct" decision (True).
        decision = juror1 if (juror1 == juror2) else juror3
        if decision:
            correct += 1

    average = correct / samples
    print("Probability of correct decision:", average)


if __name__ == '__main__':
    flippant_juror()
