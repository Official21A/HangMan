from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

from random_words import RandomWords
from functools import partial
import sys

import headers as H


# to create a database of words in each game
r = RandomWords() 

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


class GameView(QMainWindow): # the game view
    def __init__(self): # class initializer
        super().__init__()
        
        self.setWindowTitle('Hang Man')
        self.setFixedSize(600, 500)
        
        self.generalLayout = QVBoxLayout() # the window base layout

        self._centralWidget = QWidget(self) # need to add this to centera
        self.setCentralWidget(self._centralWidget)

        self.generalLayout.setContentsMargins(10, 0, 0, 10)
        self._centralWidget.setLayout(self.generalLayout)
        
        self.__create_display__() # managing the components
        self.__create_buttons__()

        self.setDisplayText()
        self.updateDisplay()

    def __create_display__(self):
    	# this method will create and put components in their places
        self.display = QLineEdit()
        self.inputLayout = QHBoxLayout()
        self.input = QLineEdit()
        self.label = QLabel()
        self.imageLabel = QLabel()
        self.user_info = QLabel()

        __create_logo__()
        __set_fonts__()
        
        self.display.setFixedHeight(100)
        self.display.setFixedWidth(580)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignCenter)

        self.inputLayout.setContentsMargins(0, 30, 10, 30)
        self.input.setFixedHeight(35)
        self.label.setText("Enter your guess : ")
        self.inputLayout.addWidget(self.label)
        self.inputLayout.addWidget(self.input)

        self.user_info.setFixedHeight(35)
        self.user_info.setAlignment(Qt.AlignCenter)

        self.generalLayout.addWidget(self.imageLabel)
        self.generalLayout.addWidget(self.display)
        self.generalLayout.addWidget(self.user_info)
        self.generalLayout.addLayout(self.inputLayout)

    def __create_logo__(self): 
    	# this method creates the game top logo
        self.image = QPixmap("logo.png");
        self.image = self.image.scaled(500, 200)
        self.imageLabel.setPixmap(self.image)
        self.imageLabel.setAlignment(Qt.AlignCenter) 

    def __set_fonts__(self):
    	# this method sets the font sizes of the components
    	display_size, normal_size = 20, 16

    	font = self.display.font()   
        font.setPointSize(display_size)             
        self.display.setFont(font)

        font = self.input.font()      
        font.setPointSize(normal_size) 
        self.input.setFont(font)

        font = self.user_info.font()      
        font.setPointSize(normal_size) 
        self.user_info.setFont(font)

    def __create_buttons__(self):
    	# this method creates the game buttons
    	size_tuple = (100, 40)

    	buttonsLayout = QGridLayout()
    	self.cancel = QPushButton("DELETE")
    	self.hint = QPushButton("HINT")
    	self.enter = QPushButton("ENTER")
    	self.quit = QPushButton("QUIT")

    	self.cancel.setFixedSize(size_tuple)
    	buttonsLayout.addWidget(self.cancel, 0, 0)
    	self.cancel.setStyleSheet("background-color:#ff3333");

    	self.hint.setFixedSize(size_tuple)
    	buttonsLayout.addWidget(self.hint, 0, 1)
    	self.hint.setStyleSheet("background-color:#ffff66");

    	self.quit.setFixedSize(size_tuple)
    	buttonsLayout.addWidget(self.quit, 1, 0)
    	self.quit.setStyleSheet("background-color:#e60000");

    	self.enter.setFixedSize(size_tuple)
    	buttonsLayout.addWidget(self.enter, 1, 1)
    	self.enter.setStyleSheet("background-color:#4dff4d");

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
    	global game

    	if input_string == "get()":
    		input_string = self._view.input.text().lower()	
    	elif input_string == "quit()":
    		sys.exit(0)

    	__main_process__(input_string)

    	self._view.setDisplayText()
    	self._view.updateDisplay()
    	self._view.clearDisplay()

    	if not game:
    		self.dialog.show()	


class Dialog: # this class showsup when the game is over	 	
	def show(self):
		global main_word

		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText(f"The word was \"{main_word}\". Press OK to quit.")
		msg.setWindowTitle("HangMan")

		msg.setStandardButtons(QMessageBox.Ok)
		 
		msg.exec_()
		msg.buttonClicked.connect(sys.exit(0))  	


def main():
	# program runner
    global main_word
    hm_app = QApplication(sys.argv)
    
    view = GameView()
    view.show()
    
    Controller(view=view)
    print(main_word)
    
    sys.exit(hm_app.exec_())


if __name__ == '__main__':
    main() # Execute    
