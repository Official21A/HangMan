from random_words import RandomWords
from colorama import Fore
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
game_hints = 100

main_word = r.random_word()
word_len = len(main_word)
game_limit = word_len
bool_index = [False for i in range(2 * word_len)]


def __main_process__(char):
	# this function is the game check loop
	global game
	global counter
	global game_limit
	global game_hints
	global main_word
	global bool_index
	if len(char) == 1:
		indexes = H.search(main_word, char)

		if len(indexes) != 0:
			# the string contains the user char input
			H.update(bool_index, indexes)
			counter += len(indexes)0
	else:
		# less or more than one words compare differently
		if char == main_word:
			game = False	

		if char == "hint()":
			if game_hints > 0:
				H.hint(bool_index, main_word)	
				game_hints -= 1
				game_limit += 1
				counter += 1

	if counter == word_len:
		game = False

	if game_limit == 0:
		game = False

	game_limit -= 1	


def word_output():
	global main_word
	global bool_index
	string = []
	word = list(main_word)
	for i in range(len(bool_index)):
		if i % 2 == 1:	
			string.append(" ")
		else:
			if bool_index[i]:
				string.append(word[i / 2])
			else:
				string.append("_")	
	return "".join(string)			


class HmGui(QMainWindow):
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

    def _createDisplay(self):
    	self.display = QLineEdit()
        self.input = QLineEdit()
        self.user_info = QLabel()
        
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)

        self.input.setFixedHeight(35)
        self.input.setFixedWidth(100)

        self.user_info.setFixedHeight(35)
        self.user_info.setFixedWidth(50)
        self.user_info.setAlignment(Qt.AlignCenter)

        self.generalLayout.addWidget(self.display)
        self.generalLayout.addWidget(self.user_info)
        self.generalLayout.addWidget(self.input)

    def _createButtons(self):
    	buttonsLayout = QGridLayout()
    	cancel = QPushButton("DELETE")
    	hint = QPushButton("HINT")
    	enter = QPushButton("ENTER")

    	cancel.setFixedSize(80, 40)
        buttonsLayout.addWidget(cancel, 0, 0, 1, 0)

        hint.setFixedSize(40, 40)
        buttonsLayout.addWidget(hint, 0, 1)

        enter.setFixedSize(40, 40)
        enter.addWidget(cancel, 1, 1)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText():
        self.display.setText(word_output())
        self.input.setFocus()

    def displayText(self):
        return self.input.text()

    def clearDisplay(self):
        self.input.setText('').lower()

    def updateDisplay(self):
    	string = f"Hints {game_hints} / Turns {game_limit}" 
    	self.user_info.setText(string)  


class HmController:
	def __init__(self, view, model):
        self._view = view
        self._input = model

        self._connectSignals()

    def _connectSignals(self):
    	cancel.clicked.connect(self._view.clearDisplay())
    	hint.clicked.connect(partial(self.click_btn, "hint()"))
    	enter.clicked.connect(partial(self.click_btn, self._view.displayText()))
    	
    def click_btn(self, char):
    	partial(_input, char)
    	self._view.setDisplayText()
    	self._view.updateDisplay()	


def main():
