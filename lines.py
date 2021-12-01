


class Line():
  def __init__(self, blockSize) -> None:
    self.valid = 0
    self.dirty = 0
    self.tag = "00"
    self.block = ['00' for i in range(blockSize)]

  def attributes(self):
    return (self.dirty, self.valid, self.tag, self.block)

  def update_line(self, tag, offset, data):
    self.valid = 1
    self.tag = tag
    self.block = data
