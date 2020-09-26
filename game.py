import random

from headers import find, clear, sleep


word_list_data = ['data', 'port', 'admin'] # data words for the game

main_word = random.choice(word_list_data)

word_len = len(main_word)
counter = 0
game = True

while game == True:
	sleep()
	clear()
	# main while of the game
	char = input("Guess >> ")

	if len(char) == 1:
		indexes = find(main_word, char)

		if len(indexes) != 0:
			# the string contains the user char input
			print(f"It has {len(indexes)} {char}.")
			counter += len(indexes)
		else:
			# no char in string
			print(f"No {char}.")	
	else:
		# less or more than one words compare differently
		if char == main_word:
			print("Correct")
			game = False
		else:
			print("Incorrect")	
			
	if counter == word_len:
		game = False

print(main_word)						
