# Painting Puzzle
# You play a game with four balls: One ball is red, one is blue,
# one is green and one is yellow. They are placed in a box.
# You draw a ball out of the box at random and note its color.
# Without replacing the first ball, you draw a second ball and
# then paint it to match the color of the first. Replace both balls,
# and repeat the process. The game ends when all four balls have
# become the same color. What is the expected number of turns to
# finish the game?
# From: https://fivethirtyeight.com/features/can-you-solve-these-colorful-puzzles/

import random

def painting_puzzle():
    samples = 10000
    turns = 0

    for i in range(samples):
        colors = ["red", "blue", "green", "yellow"]

        while not all_the_same(colors):
            i = random.randint(0, 3)
            colors.remove(colors[i])

            j = random.randint(0, 2)
            color = colors[j]
            colors.append(color)

            turns += 1

    average = turns / samples
    print("Expected number of turns:", average)


def all_the_same(colors):
    if ((colors[0] == colors[1]) and
           (colors[0] == colors[2]) and
           (colors[0] == colors[3])):
           return True
    else:
        return False
    

if __name__ == '__main__':
    painting_puzzle()
