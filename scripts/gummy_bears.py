# Gummy Bears
#
# There are 12 flavors of gummy bears. Assume evenly represented.
# If I have a bag of 120 gummy bears, what are the chances that if
# I select 5 random ones, each of the 5 will be different flavors?
#
# From: https://twitter.com/BecomingDataSci/status/826635249341911044

import random

def gummy_bears():
    samples = 10000
    wins = 0

    # simulate a bag with 120 items and 12 different flavors
    bag = [(x % 12) for x in range(120)]

    for i in range(samples):
        random.shuffle(bag)

        # Are the first 5 flavors unique?
        if(len(set(bag[0:5])) == 5):
            wins += 1

    average = wins / samples
    print("Probability of 5 different flavors:", average)
        


if __name__ == '__main__':
    gummy_bears()
