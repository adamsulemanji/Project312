# File: lines.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements lines.py file


class Line():
  def __init__(self, blockSize) -> None:
    self.valid = 0
    self.dirty = 0
    self.tag = "00"
    self.block = ['00' for i in range(blockSize)]
    self.readIndex = 0

  def attributes(self):
    return (self.dirty, self.valid, self.tag, self.block, self.readIndex)

  def update_line(self, tag, data, dirty, readIndex):
    self.valid = 1
    self.tag = tag
    self.block = data
    self.dirty = dirty
    self.readIndex = readIndex

  def flush(self, blockSize):
    self.__init__(blockSize)