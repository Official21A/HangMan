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

main_word = r.random_word()
word_len = len(main_word)
game_limit = 2 * word_len
game_hints = int(word_len / 2)
bool_index = [False for i in range(2 * word_len)]


def __main_process__(char):
	# this function is the game check loop
	global game
	global counter
	global game_limit
	global game_hints
	global main_word
	global bool_index

	if not game:
		return

	if len(char) == 1:
		indexes = H.search(main_word, char)

		if len(indexes) != 0:
			# the string contains the user char input
			H.update(bool_index, indexes)
			counter += len(indexes)
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
			else:
				return	

	if counter == word_len:
		game = False

	if game_limit == 0:
		game = False
		game_limit += 1

	game_limit -= 1	


def word_output():
	global main_word
	global bool_index
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
        self.setDisplayText()
        self.updateDisplay()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.input = QLineEdit()
        self.user_info = QLabel()
        
        self.display.setFixedHeight(50)
        self.display.setFixedWidth(480)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)
        font = self.display.font()      # lineedit current font
        font.setPointSize(20)               # change it's size
        self.display.setFont(font) 

        self.input.setFixedHeight(35)

        self.user_info.setFixedHeight(35)
        font = self.user_info.font()      # lineedit current font
        font.setPointSize(16) 
        self.user_info.setFont(font)
        self.user_info.setAlignment(Qt.AlignCenter)

        self.generalLayout.addWidget(self.display)
        self.generalLayout.addWidget(self.user_info)
        self.generalLayout.addWidget(self.input)

    def _createButtons(self):
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
        self.display.setText(word_output())
        self.input.setFocus()

    def clearDisplay(self):
        self.input.setText('')

    def updateDisplay(self):
    	string = f">> {game_limit} Turns remain <<" 
    	self.hint.setText(f"{game_hints} Hints")
    	self.user_info.setText(string)  


class HmController:
    def __init__(self, view, model):
        self._view = view
        self._input = model

        self._connectSignals()

    def _connectSignals(self):
    	self._view.cancel.clicked.connect(self._view.clearDisplay)
    	self._view.hint.clicked.connect(partial(self.click_btn, "hint()"))
    	self._view.enter.clicked.connect(partial(self.click_btn, "@test"))
 
    def click_btn(self, char):
    	if char == "@test":
    		char = self._view.input.text().lower()
    	print(char)	
    	__main_process__(char)
    	self._view.setDisplayText()
    	self._view.updateDisplay()
    	self._view.clearDisplay()	


def main():
    hm_app = QApplication(sys.argv)
    
    view = HmGui()
    view.show()
    
    model = __main_process__

    HmController(model=model, view=view)
    
    sys.exit(hm_app.exec_())

if __name__ == '__main__':
    main()    
