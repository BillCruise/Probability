# Collecting coupons
# Coupons in cereal boxes are numbered 1 to 5, and a set of one
# of each is required for a prize. With one coupon per box, how
# many boxes on average are required to make a compete set?
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 14

import random

def collecting_coupons():
    samples = 10000
    total = 0

    for i in range(samples):
        coupons = [False] * 5
        count = 0
        
        while(not all(coupons)):
            r = random.randint(0, 4)
            coupons[r] = True
            count += 1

        total += count

    average = total / samples
    print("Average number of boxes to collect all 5:", average)


if __name__ == '__main__':
    collecting_coupons()
