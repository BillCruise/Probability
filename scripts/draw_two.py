# Draw Two
# Two numbers are drawn from the integers 1-10.
# What's the expected value of their sum.
# (With and without replacement.)
# Based on https://twitter.com/MrHonner/status/917546796322377728

import random

def with_replacement(samples):
    total = 0

    for i in range(samples):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = a + b
        total += c

    avg = total / samples
    return avg


def without_replacement(samples):
    total = 0

    for i in range(samples):
        values = list(range(1, 11)) # range stop value is not inclusive
        random.shuffle(values)
        a = values.pop()
        b = values.pop()
        c = a + b
        total += c

    avg = total / samples
    return avg


def draw_two():
    samples = 10000
    with_rep = with_replacement(samples)
    without_rep = without_replacement(samples)
    print("Expected value with replacement:", with_rep)
    print("Expected value without replacement:", without_rep)

if __name__ == '__main__':
    draw_two()
