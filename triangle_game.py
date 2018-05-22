#!/usr/bin/python

class Board(object):
  def __init__(self): 
    self.holes = []
    for i in range(15):
      if i==0:
        peg = 0
      else:
        peg = 1
      self.holes.append(Hole(peg=peg, move_options=[]))

    # Define move_options list 
    self.holes[0].move_options = [MoveOption(3,1), MoveOption(5,2)]
    self.holes[1].move_options = [MoveOption(6,3), MoveOption(8,4)]
    self.holes[2].move_options = [MoveOption(7,4), MoveOption(9,5)]
    self.holes[3].move_options = [MoveOption(0,1), MoveOption(5,4), MoveOption(10,6), MoveOption(12,7)]
    self.holes[4].move_options = [MoveOption(11,7), MoveOption(13,8)]
    self.holes[5].move_options = [MoveOption(0,2), MoveOption(3,4), MoveOption(12,8), MoveOption(14,9)]
    self.holes[6].move_options = [MoveOption(1,3), MoveOption(8,7)]
    self.holes[7].move_options = [MoveOption(2,4), MoveOption(9,8)]
    self.holes[8].move_options = [MoveOption(1,4), MoveOption(6,7)]
    self.holes[9].move_options = [MoveOption(2,5), MoveOption(7,8)]
    self.holes[10].move_options = [MoveOption(3,6), MoveOption(12,11)]
    self.holes[11].move_options = [MoveOption(4,7), MoveOption(13,12)]
    self.holes[12].move_options = [MoveOption(3,7), MoveOption(5,8), MoveOption(10,11), MoveOption(14,13)]
    self.holes[13].move_options = [MoveOption(4,8), MoveOption(11,12)]
    self.holes[14].move_options = [MoveOption(5,9), MoveOption(12,13)]

  def display(self):
    print("Current Board")
    i = 0
    rl = 1
    while i <=14:
      rholes=[]
      rpegs=[]
      for j in range(0,rl):
        if(self.holes[i].peg):
          rpegs.append("X")
        else:
          rpegs.append("O")
        rholes.append(i)
        i += 1
      rl += 1 
      for j in range(0,len(rpegs)):
        print(rpegs[j]),
      print("\n"),
      for j in range(0,len(rholes)):
        print(rholes[j]),
      print("\n")
    # TO DO: Make board printing prettier
 
  def game_over(self):
    for h in self.holes:
      if h.peg:
        for m in h.move_options:
          if not self.holes[m.dest].peg:
            if self.holes[m.jump_over].peg:
              print("There is at least one move available. Can jump to hole {}".format(m.dest))
              return False
              break
    return True
    # TO DO: Check this to see if this method is ok

  def get_jump_over(self,start,dest):
    for m in self.holes[start].move_options:
      if m.dest == dest:
        return m.jump_over
    # TO DO: Check to see if this method is ok
   

class Hole(object):
  def __init__(self, peg, move_options):
    self.peg = peg
    self.move_options = move_options

class MoveOption(object):
  def __init__(self, dest, jump_over):
    self.dest = dest
    self.jump_over = jump_over


# initialize board

board = Board()
#print(board) 

while True:
  board.display()
  if board.game_over():
    # check whether they won
    pegs_remaining = 0
    for h in board.holes:
      if h.peg:
        pegs_remaining += 1
    print("Game over. {} pegs remaining.".format(pegs_remaining))
    break
  else: 
    # ask for next move
    start = int(raw_input("Enter the start position: "))
    dest = int(raw_input("Enter the destination position: "))
    jump_over = board.get_jump_over(start, dest)
    if jump_over is None:
      print("Invalid move. Pick again")
    else:
      # perform move
      board.holes[start].peg = False
      board.holes[jump_over].peg = False
      board.holes[dest].peg = True
    
