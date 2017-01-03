# Trials until success
# On average, how many times must a die be thrown until one rolls a six?
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 4

import random

def trials_until_success():
    samples = 10000
    total = 0;
    
    for i in range(samples):
        throws = 1
        die = random.randint(1, 6)
        
        while(die != 6):
            die = random.randint(1, 6)
            throws += 1

        total += throws

    average = total / samples
    print("Average number of throws until the first 6: ", average)

if __name__ == '__main__':
    trials_until_success()
