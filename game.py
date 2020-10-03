from random_words import RandomWords
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from functools import partial

import headers as H


r = RandomWords() # data words for the game

game = True
counter = 0
game_limit = 0

main_word = r.random_word()
word_len = len(main_word)
game_limit = 2 * word_len
game_hints = int(word_len / 2)
bool_index = [False for i in range(2 * word_len)]


def __main_process__(char):
	# the game model

	global game, counter, game_limit, game_hints, main_word, bool_index 

	if not game:
		# this is when the user is out of turns or the user gussed the word
		return

	if len(char) == 1:
		# if user input was a single char
		indexes = H.search(main_word, char)

		if len(indexes) != 0:
			H.update(bool_index, indexes)
			counter += len(indexes)
	else:
		# less or more than one words compare differently
		if char == main_word:
		    H.game_done(bool_index)
		    game = False	

		if char == "hint()":
			# using the hints
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


class HmGui(QMainWindow):
	# the game view
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('HangMan')
        self.setFixedSize(500, 500)
        
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        self._createDisplay()
        self._createButtons()
        self.setDisplayText()
        self.updateDisplay()

    def _createDisplay(self):
    	# this method will create and put conmonents in their places
        self.display = QLineEdit()
        self.input = QLineEdit()
        self.user_info = QLabel()
        
        self.display.setFixedHeight(50)
        self.display.setFixedWidth(480)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)
        font = self.display.font()   
        font.setPointSize(20)             
        self.display.setFont(font) 

        self.input.setFixedHeight(35)

        self.user_info.setFixedHeight(35)
        font = self.user_info.font()      
        font.setPointSize(16) 
        self.user_info.setFont(font)
        self.user_info.setAlignment(Qt.AlignCenter)

        self.generalLayout.addWidget(self.display)
        self.generalLayout.addWidget(self.user_info)
        self.generalLayout.addWidget(self.input)

    def _createButtons(self):
    	# this method creates the game buttons
    	buttonsLayout = QGridLayout()
    	self.cancel = QPushButton("DELETE")
    	self.hint = QPushButton("HINT")
    	self.enter = QPushButton("ENTER")

    	self.cancel.setFixedSize(320, 40)
    	buttonsLayout.addWidget(self.cancel, 0, 0, 1, 0)

    	self.hint.setFixedSize(80, 40)
    	buttonsLayout.addWidget(self.hint, 1, 0)

    	self.enter.setFixedSize(80, 40)
    	buttonsLayout.addWidget(self.enter, 1, 1)

    	self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self):
    	# a method for updating the display after each iterate
        global main_word, bool_index
        self.display.setText(H.word_output(main_word, bool_index))
        self.input.setFocus()

    def clearDisplay(self):
    	# clear input
        self.input.setText('')

    def updateDisplay(self):
    	# this method updates the user information
    	string = f">> {game_limit} Turns remain <<" 
    	self.hint.setText(f"{game_hints} Hints")
    	self.user_info.setText(string)  


class HmController:
	# game controller
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _connectSignals(self):
    	# this method adds the functions to its buttons
    	self._view.cancel.clicked.connect(self._view.clearDisplay)
    	self._view.hint.clicked.connect(partial(self.click_btn, "hint()"))
    	self._view.enter.clicked.connect(partial(self.click_btn, "@test"))
 
    def click_btn(self, char):
    	# handel the button clicked
    	global game
    	if char == "@test":
    		char = self._view.input.text().lower()	
    	if not game:
    		self._view.enter.clicked.connect(sys.exit(0))
    	__main_process__(char)
    	self._view.setDisplayText()
    	self._view.updateDisplay()
    	self._view.clearDisplay()	


def main():
	# program runner
    global main_word
    hm_app = QApplication(sys.argv)
    
    view = HmGui()
    view.show()

    HmController(view=view)
    print(main_word)
    
    sys.exit(hm_app.exec_())


if __name__ == '__main__':
    main() # Execute    
