from random_words import RandomWords
from colorama import Fore

import headers as H


r = RandomWords() # data words for the game

game = True
counter = 0
game_limit = 0


def __input__(limit):
	# this function does the input getting
	global game_limit
	return input(f"\n\n  {game_limit} turns remain, Guess >> ")

def __output__(code, state):
	# this function does the output showing
	if code == 1:
		print(f"{Fore.YELLOW}No {state}.")
	elif code == 2:
		print(f"{Fore.GREEN}Correct")
	elif code == 3:
		print(f"\n{Fore.RED}Incorrect")
	elif code == 4:
		print(f"\"{state}\" was the correct word.")	
	elif code == 5:
		print(f"\n{Fore.RED}Sorry, you lost.")	
	print(f"{Fore.RESET}", end='')				


def __main_process__(char, main_word, bool_index):
	# this function is the game check loop
	global game
	global counter
	global game_limit
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

	if game_limit == 0:
		code = 5
		game = False

	game_limit -= 1	
	return code	


main_word = r.random_word()
word_len = len(main_word)
game_limit = word_len
bool_index = [False for i in range(2 * word_len)]

H.clean()

while game == True:
	# main while of the game
	H.wait()

	H.show(bool_index, main_word)

	char = __input__(word_len).lower()
	code = __main_process__(char, main_word, bool_index)
	__output__(code, char)						

__output__(4, main_word)