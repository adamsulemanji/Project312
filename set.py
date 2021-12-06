# File: set.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements set.py file


## @package pyexample
# @file set.py
# 
# @brief The file defines the class for each set which has the methods of intialization,getlines and isfull.  

## Documentation for each set
# Importing each line


import lines

class Set():
  ## Documentation for the intialization of a set
  # @param self a pointer to itself
  # @param numLines number of lines per set
  # @param blockSize the size of the block
  # @param setNumber which set number it is
  # @var self.associativity number of lines per set
  # @var self.blockSize the size of the block
  # @var self.setNumber the set number
  # @var self.lines creating the number of lines per set in each set
  def __init__(self, numLines, blockSize, setNumber):
    self.associativity = numLines
    self.blockSize = blockSize
    self.setNumber = setNumber
    self.lines = list(lines.Line(blockSize) for i in range (self.associativity))

  ## Documentation for the getLines method
  # @param self a pointer to itself
  # @return self.lines returns the lines in an indexable list fashion
  def getLines(self):
    return self.lines

  ## Documentation for the isFull method
  # @param self a pointer to itself
  # return a boolea checking whether the line is full. 
  def isFull(self):
    for line in self.lines:
      if line.attributes()[1] == 0:
        return False
    return True