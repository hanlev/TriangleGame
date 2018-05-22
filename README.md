# TriangleGame
This is a command-line game that mimics the Triangle Peg Game. 

Game Objective
--------------
In this game you have a triangle that has 15 holes (one hole in the first row, 2 holes in the second, 3 holes in the third...).
You have 14 pegs in all but one of the holes. The goal is to remove as many pegs as possible from the board.
Ideally, you will end up with only one peg left. The fewer pegs remaining when no more moves are possible, the better.

Game Rules
-----------
The way you can remove pegs is by taking a peg and jumping over an adjacent peg so that the original peg lands
in an empty hole. You remove the peg that was jumped over.
* Three pegs remaining is ok but not excellent.
* Two pegs remaining is good but still not excellent.
* One peg remaining is excellent! That is the goal.

Running the Game
------------
This game is written in Python and intended to be used at a Linux/Mac OS command line. To run the game, type 

    python TriangleGame.py

You will be given command-line prompts asking you to enter a number corresponding to a hole containing 
the peg that you want to move (that is, the peg that will be "jumping" over another peg to an empty hole).
You will also be prompted to enter a number corresponding to the empty hole where you would like the moved 
peg to land. 
