# Infinite Monkeys
#
# If infinite monkeys struck each of the 26 letters of a typewriter once,
# what is the probability that either name 'IAGO' or 'LEAR' would appear?

import random

def infinite_monkeys():
    samples = 100000
    iagos = 0
    lears = 0

    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    for i in range(samples):
        random.shuffle(alphabet)
        output = ''.join(alphabet)

        if "IAGO" in output:
            iagos += 1

        if "LEAR" in output:
            lears += 1

        
    average = (iagos + lears) / samples
    print("Probability that 'IAGO' or 'LEAR' appears:", average)

    

if __name__ == '__main__':
    infinite_monkeys()
