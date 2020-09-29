# this file keeps the game main functions
import os
import time
import random


def search(s, ch):
	# this function will return the indexes of a char in a string
    return [i for i, ltr in enumerate(s) if ltr == ch]

def clean():
	# this function clears the consol
	os.system('clear')   

def wait():
	# this function is for setting a waiting time
	time.sleep(0.1)

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
