# Theater Seats
# To watch a movie, John, Mary and 5 friends will sit randomly in
# a row with 7 seats. What is the probability John and Mary won't
# sit together?

from __future__ import division
import random

def theater_seats():
    samples = 10000
    friends = [ "Alice", "Bob", "Carol", "Dave", "Eve", "John", "Mary" ]
    john_mary = 0
    mary_john = 0

    for i in range(samples):
        random.shuffle(friends)
        seating = ",".join(friends)
        if "John,Mary" in seating:
            john_mary += 1
        if "Mary,John" in seating:
            mary_john += 1

    average = (john_mary + mary_john) / samples;
    print("Mary sat next to John", john_mary + mary_john, "times.")
    print("The probability Mary won't sit next to John is", 1.0 - average)


if __name__ == '__main__':
    theater_seats()
