# The Petersburg Paradox
# http://en.wikipedia.org/wiki/St._Petersburg_paradox
# A casino offers a game of chance for a single player in which a fair coin is 
# tossed at each stage. The pot starts at 2 dollars and is doubled every time 
# a head appears. The first time a tail appears, the game ends and the player 
# wins whatever is in the pot. Thus the player wins 2 dollars if a tail appears 
# on the first toss, 4 dollars if a head appears on the first toss and a tail on 
# the second, 8 dollars if a head appears on the first two tosses and a tail on 
# the third, 16 dollars if a head appears on the first three tosses and a tail on 
# the fourth, and so on. In short, the player wins 2k dollars, where k equals number 
# of tosses. What would be a fair price to pay the casino for entering the game?

from random import random

samples = 10000
winnings = 0.0

for i in range(samples):
	pot = 2
	keep_playing = True
	
	while(keep_playing):
		if random() < 0.5: # call this heads
			pot *= 2
		else:
			winnings += pot
			keep_playing = False
			
expected_winnings = winnings / samples
print("Fair price to pay to enter the game: %.2f" % expected_winnings)