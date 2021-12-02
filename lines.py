


class Line():
  def __init__(self, blockSize) -> None:
    self.valid = 0
    self.dirty = 0
    self.tag = "00"
    self.block = ['00' for i in range(blockSize)]
    self.readIndex = 0

  def attributes(self):
    return (self.dirty, self.valid, self.tag, self.block, self.readIndex)

  def update_line(self, tag, data, readIndex):
    self.valid = 1
    self.tag = tag
    self.block = data
    self.readIndex = readIndex

  def flush(self, blockSize):
    self.__init__(blockSize)