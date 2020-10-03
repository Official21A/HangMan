# this file keeps the game main functions
import random


def search(s, ch):
	# this function will return the indexes of a char in a string
    return [i for i, ltr in enumerate(s) if ltr == ch] 

def update(bool_index, indexes):
	# this function updates the boolean indexes
	for i in indexes:
		bool_index[2 * i] = True			

def __help__(bool_index):
	bool_list = []
	for i in range(0, len(bool_index)):
		if i % 2 == 0 and not bool_index[i]:
			bool_list.append(i)		
	return bool_list		

def hint(bool_index, word):
	# this function will show a letter to user
	bool_list = __help__(bool_index)
	if len(bool_list) == 0:
		return
	index = random.choice(bool_list)
	bool_index[index] = True	

def word_output(main_word, bool_index):
	# this function creates the string form of output
	string = []
	word = list(main_word)
	for i in range(len(bool_index)):
		if i % 2 == 1:	
			string.append("  ")
		else:
			if bool_index[i]:
				string.append(word[int(i / 2)])
			else:
				string.append("_")	
	return "".join(string)	

def game_done(bool_index):
	for i in range(len(bool_index)):
		if i % 2 == 0:
			bool_index[i] = True					
