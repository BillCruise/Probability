# The Theater Row
# Eight eligible bachelors and seven beautiful models
# happen randomly to have purchased single seats in a
# 15-seat row of a theater. On the average, how many pairs
# of adjacent seats are ticketed for marriageable couples?
#
# From: Fifty Challenging Problems in Probability
#       by Frederic Mosteller
#       Problem 15

import random

def theater_row():
    samples = 10000
    total = 0

    brides = [False] * 7
    grooms = [True] * 8
    row = brides + grooms
    
    for i in range(samples):
        random.shuffle(row)
        total += couples(row)

    average = total / samples
    print("Average number of couples in the row:", average)

# find how many couples there are in the row
def couples(row):
    a = 0
    b = 1
    count = 0
    
    while(b < len(row)):
        if(row[a] != row[b]):
            count += 1
        a += 1
        b += 1

    return count
        


if __name__ == '__main__':
    theater_row()
