# All Aboard
#
# One hundred people board a 100-seat airplane. The first one has lost
# his boarding pass, so he sits in a random seat. Each subsequent
# passenger sits in his own seat if it’s available or takes a random
# unoccupied seat if it’s not.
# What’s the probability that the 100th passenger finds his seat occupied?
#
# From: Futility Closet
# http://www.futilitycloset.com/2012/02/29/all-aboard-5/

import random

def all_aboard():
    samples = 10000
    total = 0
    num_passengers = 100

    for i in range(samples):
        seats = [s for s in range(num_passengers)]
        passengers = [p for p in range(num_passengers)]
        random.shuffle(passengers)

        # pop the first passenger, but have them occupy a random seat
        passengers.pop()
        seat = random.randint(0, num_passengers-1)
        seats.remove(seat)

        # seat the next 98 passengers
        for j in range(len(passengers) - 1):
            if passengers[j] in seats:
                seats.remove(passengers[j])
            else:
                seats.pop(random.randint(0, len(seats)-1))

        # is the last passenger's seat available?
        if passengers[len(passengers)-1] != seats[0]:
            total += 1

    average = total / samples
    print("Probability that the 100th passenger finds his seat occupied:", average)
        

if __name__ == '__main__':
    all_aboard()
