import random

import headers as H


word_list_data = ['data', 'port', 'admin'] # data words for the game

main_word = random.choice(word_list_data)

word_len = len(main_word)
counter = 0
game = True

bool_index = [False for i in range(2 * word_len)]

H.clean()

while game == True:
	# main while of the game
	H.wait()

	H.show(bool_index, main_word)

	char = input("\n\n\tGuess >> ")

	if len(char) == 1:
		indexes = H.search(main_word, char)

		if len(indexes) != 0:
			# the string contains the user char input
			H.update(bool_index, indexes)
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
