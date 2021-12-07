# File: lines.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements lines.py file

## Documentation for the lines class and its respective methods
# 
# @file lines.py
#
# @brief The function defines the class for each line in the cache and its respectives methods

## Documentation for each line and its respective methods
class Line():
  ## The constructor for each line
  # @param blockSize the block size of the cache
  # @param self a pointer to itself
  # @var self.valid the validity of the line
  # @var self.dirty indicates wheter or not the corresponding block of memory has been modified
  # @var self.tag contains the address of the actual data fetched from the main memory
  # @var self.block contains the actual information fetched from the main memory
  # @var self.readIndex contains the readIndex information
  def __init__(self, blockSize) -> None:
    ## the validity of the line
    self.valid = 0
    ## indicates wheter or not the corresponding block of memory has been modified
    self.dirty = 0
    ## contains the address of the actual data fetched from the main memory
    self.tag = "00"
    ## contains the actual information fetched from the main memory
    self.block = ['00' for i in range(blockSize)]
    ## contains the readIndex information
    self.readIndex = 0


  ## Documentation for the return statement of the block
  # @param self A pointer to itself
  # @retval Returns all attributes of itself in an indexable fashion
  # @code
  # def attributes(self):
  #   return (self.dirty, self.valid, self.tag, self.block, self.readIndex)
  # @endcode
  def attributes(self):
    return (self.dirty, self.valid, self.tag, self.block, self.readIndex)



  ## Documentation for updating line
  # @param self A pointer to itself
  # @param tag the new tag
  # @param data the new data
  # @param dirty the new dirty bit (checks to see whether the infomration was previosuly changed)
  # @param readIndex the new readIndex
  # @code
  # def update_line(self, tag, data, dirty, readIndex):
  #   self.valid = 1
  #   self.tag = tag
  #   self.block = data
  #   self.dirty = dirty
  #   self.readIndex = readIndex
  # @endcode
  def update_line(self, tag, data, dirty, readIndex):
    self.valid = 1
    self.tag = tag
    self.block = data
    self.dirty = dirty
    self.readIndex = readIndex

  ## Documentation for the flush function whic
  # @param self A pointer to itself
  # @param blockSize The new and updated block size
  # @code
  # def flush(self, blockSize):
  #   self.__init__(blockSize)
  # @endcode
  def flush(self, blockSize):
    self.__init__(blockSize)