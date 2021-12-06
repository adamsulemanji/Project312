# File: lines.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements lines.py file

## 
# @package pyexample
# @file lines.py
#
# @brief The function defines the class for each line in the cache and its respectives methods


class Line():

  ## The constructor for each line
  # @param blockSize the block size of the cache
  # @param self a pointer to itself
  # @var self.valid the validity of the line
  # @var self.dirty indicates wheter or not the corresponding block of memory has been modified
  # @var self.tag contains the address of teh actual data detched from the main memory
  # @var self.block contains the actual information fetched from the main memory
  # @var self.readIndex contains the readIndex information
  def __init__(self, blockSize) -> None:
    self.valid = 0
    self.dirty = 0
    self.tag = "00"
    self.block = ['00' for i in range(blockSize)]
    self.readIndex = 0


  ## Documentation for the return statement of the block
  #  @param self a pointer to itself
  #  @return returns all attributes of itself in an indexable fashion
  def attributes(self):
    return (self.dirty, self.valid, self.tag, self.block, self.readIndex)

  ## Documentation for updating line
  # @param self a pointer to itself
  # @param tag the new tag
  # @param data the new data
  # @param dirty the new dirty bit (checks to see whether the infomration was previosuly changed)
  # @param readIndex the new readIndex
  def update_line(self, tag, data, dirty, readIndex):
    
    self.valid = 1
    self.tag = tag
    self.block = data
    self.dirty = dirty
    self.readIndex = readIndex

  ## Documentation for the flush function
  # @param self a pointer to itself
  # @param blockSize the new and updated block size
  def flush(self, blockSize):
    self.__init__(blockSize)