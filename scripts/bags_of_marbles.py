# Bags of Marbles
# You have three identical bags, each containing two marbles.
# Bag A contains two white marbles, bag B contains two black marbles,
# and Bag C contains one white and one black marble.
# You pick a bag at random and draw out one marble. If the marble is white,
# what is the probability that the other marble in the same bag
# is also white?

from __future__ import division
import random

def bags_of_marbles():
    samples = 10000
    white_1 = 0
    white_2 = 0

    for i in range(samples):
        bag_a = [ "white", "white" ]
        bag_b = [ "black", "black" ]
        bag_c = [ "white", "black" ]

        # select a bag at random
        b = random.randint(1, 3)
        if b == 1:
            bag = bag_a
        elif b == 2:
            bag = bag_b
        else:
            bag = bag_c

        # pick a marble from the bag
        marble_1 = bag.pop(random.randint(0, 1))
        if marble_1 == "white":
            white_1 += 1
            # look at the other marble
            marble_2 = bag.pop()
            if marble_2 == "white":
                white_2 += 1

    print("First marble was white", white_1, "times.")
    print("Second marble was white", white_2, "times.")
    print("Probability that 2nd marble was white when 1st marble was white:", white_2 / white_1)
            
            

if __name__ == '__main__':
    bags_of_marbles()
