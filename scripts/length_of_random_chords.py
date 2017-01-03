# Lengths of Random Chords
# If a chord is selected at random on a fixed circle, what is the probability
# that its length exceeds the radius of the circle?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 25

import random
import math

def length_of_random_chords():
    samples = 10000
    positive = 0
    radius = 0.5  # assume a unit circle

    for i in range(samples):
        angle = random.random() * 2 * math.pi
        p1 = calc_point(angle, radius)

        angle = random.random() * 2 * math.pi
        p2 = calc_point(angle, radius)

        if distance(p1, p2) > 0.5:
            positive += 1

    average = positive / samples
    print("Probability that a random chord exceeds the radius:", average)
        

# calculate a point on a circle given
# an angle in radians and its radius
def calc_point(angle, radius):
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    return (x, y)


# calculate the distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == '__main__':
    length_of_random_chords()
