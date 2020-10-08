# HangMan
The old hangman game with python "Qt" user interface.

# Introduction
Welcome to the old Hangman game, where you need to guess a word by letters or itself.
The game itself is easy and basically you can write it into a consol page, but
in this project I used the python Qt which is a user interface, so the game bacomes more
like a computer game.

Designed very easily that you can clone the project and read the codes without any helps.
I tried to use all of a GUI components that we need in a program in this codes.

If you want to know all the components and get a complete knowledge about pyQt check these links:
```

https://build-system.fman.io/pyqt5-tutorial
https://realpython.com/python-pyqt-gui-calculator/

```

# Tools
All tools we need for this project is the pyQt library with sys library which is installed, but pyQt
is not installed on your systems, so you have to install it.

Just follow these steps:

1.
```
python3 -m venv venv 
```
2.
```
source venv/bin/activate
```
3.
```
pip install PyQt5==5.9.2
```

# How it works
Our project uses MVC model. So the "view.py" is our user interface file, where we keep the codes
of creating the window that user sees and getting the users inputs.

Most of the programs pyQt usage is in this file.

Next we have the models file, where we keep the games functions. These functions are special part
of the program, cause without theme the game does not work correctly.
If you want to get a good idea of how to write a model file, check this file.

And the last but not least, the index file. Index file containes a main_process function and a controller
to get the users inputs and send them to game functions to process the data and will come with a responed
based on what the user gives. The controller will have a third person role in this program, it gets data
from gui and gives it to model and recives response from model and the gives it back to gui.

So these three parts are everything we used in this project.

# Better Design

Contact me at : najafizadeh21@gmail.com or officialamirhossein21@gmail.com
