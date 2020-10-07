from PyQt5.QtWidgets import QApplication
from random_words import RandomWords
from functools import partial
import sys

import models as H
from view import GameView, Dialog


# to create a database of words in each game
r = RandomWords() 

def __start__():
	# this function creates the start needs of the game
	global game, counter, game_limit, main_word, word_len
	global game_hints, bool_index, r

	game = True
	counter = 0
	game_limit = 0

	main_word = r.random_word() # choose one word from data base
	word_len = len(main_word)
	game_limit = 2 * word_len
	game_hints = int(word_len / 2)
	# we use boolean indexing for showing the words in output
	bool_index = [False for i in range(2 * word_len)]


def __main_process__(input_string): # the game model
	global game, counter, game_limit, game_hints, main_word, bool_index 

	if len(input_string) == 1: # if user input was a single char
		indexes = H.search(main_word, input_string)

		if len(indexes) != 0:
			H.update(bool_index, indexes)
			counter += len(indexes)
	else: # less or more than one words compare differently

		if input_string == main_word:
		    H.game_done(bool_index)
		    game = False	
		elif input_string == "hint()": # using the hints
			if game_hints > 0:
				H.hint(bool_index, main_word)	
				game_hints -= 1
				game_limit += 1
				counter += 1
			else:
				return	

	if counter == word_len:
		game = False

	if game_limit == 0:
		game = False
		game_limit += 1

	game_limit -= 1	


class Controller: # game controller
    def __init__(self, view): # class initializer
        self._view = view
        self.dialog = Dialog()
        self._connectSignals()

    def _connectSignals(self):
    	# this method adds the functions to its buttons
    	self._view.cancel.clicked.connect(self._view.clearDisplay)
    	self._view.quit.clicked.connect(partial(self.click_btn, "quit()"))
    	self._view.hint.clicked.connect(partial(self.click_btn, "hint()"))
    	self._view.enter.clicked.connect(partial(self.click_btn, "get()"))
 
    def click_btn(self, input_string): # handel the button clicked
    	global game, main_word, bool_index, game_limit, game_hints

    	if input_string == "get()":
    		input_string = self._view.input.text().lower()	
    	elif input_string == "quit()":
    		sys.exit(0)

    	__main_process__(input_string)

    	self._view.setDisplayText(H.word_output(main_word, bool_index))
    	self._view.updateDisplay(game_limit, game_hints)
    	self._view.clearDisplay()

    	if not game:
    		result = self.dialog.show(main_word)	
    		if result == "restart()":
    			self._view.close()
    			  

def main():
	# program runner
    global main_word, game_limit, game_hints, bool_index

    hm_app = QApplication(sys.argv)
    
    while True:
    	view = GameView(game_limit,game_hints,H.word_output(main_word, bool_index))
    	view.show()
    
    	Controller(view=view)
    	print(main_word)
    
    	hm_app.exec_()

    	__start__() 


if __name__ == '__main__':
    __start__()
    main() # Execute    
