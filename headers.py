# this file keeps the game main functions
import os
import time


def search(s, ch):
	# this function will return the indexes of a char in a string
    return [i for i, ltr in enumerate(s) if ltr == ch]

def clean():
	# this function clears the consol
	os.system('clear')   

def wait():
	# this function is for setting a waiting time
	time.sleep(0.5)

def update(bool_index, indexes):
	# this function updates the boolean indexes
	for i in indexes:
		bool_index[2 * i] = True		

def show(bool_index, word):
	# this function prints the current status of word
	word_len = len(word)	
	print()
	for i in range(2 * word_len):
		if i % 2 == 1:
			print("", end=' ')
		else:
			if bool_index[i] == True:
				index = int(i / 2)
				print(word[index], end = ' ')	
			else:
				print("_", end = ' ')				
