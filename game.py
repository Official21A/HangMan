import random
from colorama import Fore

import headers as H


word_list_data = ['data', 'port', 'admin'] # data words for the game

game = True
counter = 0


def __input__():
	# this function does the input getting
	return input("\n\n\tGuess >> ")

def __output__(code, state):
	# this function does the output showing
	if code == 1:
		print(f"\nNo {state}.")
	elif code == 2:
		print("\nCorrect")
	elif code == 3:
		print("\nIncorrect")
	elif code == 4:
		print(f"\"{state}\" was the correct word.")				


def __main_process__(char, main_word, bool_index):
	# this function is the game check loop
	global game
	global counter
	code = -1
	if len(char) == 1:
		indexes = H.search(main_word, char)

		if len(indexes) != 0:
			# the string contains the user char input
			H.update(bool_index, indexes)
			counter += len(indexes)
			code = 0
		else:
			# no char in string
			code = 1	
	else:
		# less or more than one words compare differently
		if char == main_word:
			code = 2
			game = False
		else:
			code = 3	

	if counter == word_len:
		code = 2
		game = False

	return code	


main_word = random.choice(word_list_data)
word_len = len(main_word)
bool_index = [False for i in range(2 * word_len)]

H.clean()

while game == True:
	# main while of the game
	H.wait()

	H.show(bool_index, main_word)

	char = __input__().lower()
	code = __main_process__(char, main_word, bool_index)
	__output__(code, char)						

__output__(4, main_word)