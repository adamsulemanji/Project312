# File: set.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements set.py file
import lines

class Set():

  def __init__(self, numLines, blockSize, setNumber):
    self.associativity = numLines
    self.blockSize = blockSize
    self.setNumber = setNumber
    self.lines = list(lines.Line(blockSize) for i in range (self.associativity))

  def getLines(self):
    return self.lines

  def isFull(self):
    for line in self.lines:
      if line.attributes()[1] == 0:
        return False
    return True