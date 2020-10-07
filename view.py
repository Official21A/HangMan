from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

import sys


class GameView(QMainWindow): # the game view
    def __init__(self, game_limit, game_hints, string): # class initializer
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

        self.setDisplayText(string)
        self.updateDisplay(game_limit, game_hints)

    def __create_display__(self):
    	# this method will create and put components in their places
        self.display = QLineEdit()
        self.inputLayout = QHBoxLayout()
        self.input = QLineEdit()
        self.label = QLabel()
        self.imageLabel = QLabel()
        self.user_info = QLabel()

        self.__create_logo__()
        self.__set_fonts__()
        
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
        self.image = QPixmap("img/logo.png");
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

    	self.cancel.setFixedSize(size_tuple[0], size_tuple[1])
    	buttonsLayout.addWidget(self.cancel, 0, 0)
    	self.cancel.setStyleSheet("background-color:#ff3333");

    	self.hint.setFixedSize(size_tuple[0], size_tuple[1])
    	buttonsLayout.addWidget(self.hint, 0, 1)
    	self.hint.setStyleSheet("background-color:#ffff66");

    	self.quit.setFixedSize(size_tuple[0], size_tuple[1])
    	buttonsLayout.addWidget(self.quit, 1, 0)
    	self.quit.setStyleSheet("background-color:#e60000");

    	self.enter.setFixedSize(size_tuple[0], size_tuple[1])
    	buttonsLayout.addWidget(self.enter, 1, 1)
    	self.enter.setStyleSheet("background-color:#4dff4d");

    	self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, string):
    	# a method for updating the display after each iterate
        self.display.setText(string)
        self.input.setFocus()

    def clearDisplay(self):
    	# clear input
        self.input.setText('')

    def updateDisplay(self, game_limit, game_hints):
    	# this method updates the user information
    	string = f">> {game_limit} Turns remain <<" 
    	self.hint.setText(f"{game_hints} Hints")
    	self.user_info.setText(string)  


class Dialog: # this class showsup when the game is over	 	
	def show(self, main_word):
		self.main_word = main_word

		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText(f"The word was \"{main_word}\". Press OK to quit.")
		msg.setWindowTitle("HangMan")

		msg.setStandardButtons(QMessageBox.Ok)

		msg.exec_()
		msg.buttonClicked.connect(sys.exit(0))  	