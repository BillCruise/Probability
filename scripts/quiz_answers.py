# Quiz Answers
# Say you're writing a math quiz game, and for each question,
# you want to present three possible answers. A naive approach to
# generating the possible answers would be to calculate the correct
# answer, then adding/subtracting a random amount to that for the
# wrong answers. Even the most inattentive players would eventually
# learn to just pick the middle answer.
# Create a strategy for automatically generating answers so that
# the correct answer is the lowest choice 1/3 of the time, the middle
# choic 1/3 of the time, and the highest choice 1/3 of the time.

import random

def quiz_answers():
    samples = 10000
    lowest = 0
    middle = 0
    highest = 0

    for i in range(samples):
        x = random.randint(1, 10)
        y = random.randint(1, 10)

        correctAns = x + y

        # strategy for generating wrong answers
        prob = random.random()
        if prob < 0.3333:
            wrongAns1 = correctAns + random.randint(1, 5)
            wrongAns2 = correctAns + random.randint(1, 5)
        elif prob < 0.6666:
            wrongAns1 = correctAns + random.randint(1, 5)
            wrongAns2 = correctAns - random.randint(1, 5)
        else:
            wrongAns1 = correctAns - random.randint(1, 5)
            wrongAns2 = correctAns - random.randint(1, 5)
            

        if correctAns < wrongAns1 and correctAns < wrongAns2:
            lowest += 1
        elif correctAns > wrongAns1 and correctAns > wrongAns2:
            highest += 1
        else:
            middle += 1

    print("Correct answer is lowest:", lowest/samples)
    print("Correct answer is middle:", middle/samples)
    print("Correct answer is highest:", highest/samples)


if __name__ == '__main__':
    quiz_answers()
