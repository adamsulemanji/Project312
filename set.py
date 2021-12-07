# File: set.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements set.py file


## 
# @file set.py
# 
# @brief The file defines the class for each set which has the methods of intialization, getlines and isfull.  
#
#
# @author Adam Sulemanji
# @author Tristan Nigos


import lines

## Documentation for each set and its methods
class Set():
  ## Documentation for the intialization of a set
  # @param self a pointer to itself
  # @param numLines number of lines per set
  # @param blockSize the size of the block
  # @param setNumber which set number it is
  # @var associativity number of lines per set
  # @var blockSize the size of the block
  # @var setNumber the set number
  # @var lines creating the number of lines per set in each set
  # @code
  #   def __init__(self, numLines, blockSize, setNumber):
  #   self.associativity = numLines
  #   self.blockSize = blockSize
  #   self.setNumber = setNumber
  #   self.lines = list(lines.Line(blockSize) for i in range (self.associativity))
  # @endcode
  def __init__(self, numLines, blockSize, setNumber):
    ## Number of lines per set
    self.associativity = numLines
    ## The size of the block
    self.blockSize = blockSize
    ## The set Number
    self.setNumber = setNumber
    ## Lines that hold information
    self.lines = list(lines.Line(blockSize) for i in range (self.associativity))


  ## Documentation for the getLines method which return all the lines in the set
  # @param self A pointer to itself
  # @retval self.lines Returns the lines in an indexable list fashion for the set
  # @code
  # def getLines(self):
  #   return self.lines
  # @endcode
  def getLines(self):
    return self.lines



  ## Documentation for the isFull method
  # @param self A pointer to itself
  # @retval Returns False if there exists a line in the set which is not full
  # @retval Returns True if all lines in the set are occupied 
  # @code
  # def isFull(self):
  #   for line in self.lines:
  #     if line.attributes()[1] == 0:
  #       return False
  #   return True
  # @endcode
  def isFull(self):
    for line in self.lines:
      if line.attributes()[1] == 0:
        return False
    return True