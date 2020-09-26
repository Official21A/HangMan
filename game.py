import random

def __find__(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

word_list_data = ['data', 'port', 'admin']

main_word = random.choice(word_list_data)

word_len = len(main_word)
counter = 0
game = True

while game == True:
	char = input("Guess >> ")
	if len(char) == 1:
		indexes = __find__(main_word, char)
		if len(indexes) != 0:
			print(f"It has {len(indexes)} {char}.")
			counter += len(indexes)
		else:
			print(f"No {char}.")	
	else:
		if char == main_word:
			print("Correct")
			game = False
		else:
			print("Incorrect")	
	if counter == word_len:
		game = False

print("Finish")						
