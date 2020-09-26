# this file keeps the game main functions
import os
import time


def find(s, ch):
	# this function will return the indexes of a char in a string
    return [i for i, ltr in enumerate(s) if ltr == ch]

def clear():
	os.system('clear')   

def sleep():
	time.sleep(2)
