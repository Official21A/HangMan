# this file keeps the game main functions


def __find__(s, ch):
	# this function will return the indexes of a char in a string
    return [i for i, ltr in enumerate(s) if ltr == ch]