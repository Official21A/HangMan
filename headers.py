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

def print(bool_index, word):
	word_len = len(word)	
	for i in range(2 * word_len):
		if i % 2 == 1:
			print("", end=' ')
		else:
			if bool_index[i] == True:
				print(word[i / 2], end=' ')	
			else
				print("_", end=' ')	
