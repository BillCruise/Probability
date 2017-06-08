# Dicey Question
# You are about to roll five regular dice. You win if you roll exactly
# one six. You lose if you roll no sixes. Are you more likely to win
# than lose, or are you less likely to win than lose?

import random

def dicey_question():
    samples = 10000
    wins = 0
    losses = 0

    for i in range(samples):
        sixes = 0
        for j in range(5):
            d = random.randint(1, 6)
            if d == 6:
                sixes += 1

        
        if sixes == 1:
            wins += 1

        if sixes == 0:
            losses += 1

    
    avg_wins = wins / samples
    avg_loss = losses / samples
    print("Chance of winning:", avg_wins)
    print("Chance of losing:", avg_loss)



if __name__ == '__main__':
    dicey_question()
