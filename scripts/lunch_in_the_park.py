# Lunch in the Park
#
# On a lovely spring day, you and I agree to meet for a lunch
# picnic at the fountain in the center of our favorite park.
# We agree that we’ll each arrive sometime from noon and 1 p.m.,
# and that whoever arrives first will wait up to 15 minutes for
# the other. If the other person doesn’t show by then, the first
# person will abandon the plans and spend the day with a more
# punctual friend. If we both arrive at the fountain at an
# independently random time between noon and 1, what are the
# chances our picnic actually happens?
#
# From "What Are The Chances We’ll Meet For Lunch?"
#      https://fivethirtyeight.com/features/what-are-the-chances-well-meet-for-lunch/

import random

def lunch_in_the_park():
    samples = 10000
    lunches = 0

    for i in range(samples):
        time1 = random.randint(0, 59)
        time2 = random.randint(0, 59)

        if abs(time1 - time2) <= 15:
            lunches += 1

    average = lunches / samples
    print("Chances the picnic will actually happen:", average)
    


if __name__ == '__main__':
    lunch_in_the_park()
