


class Line():
  def __init__(self, blockSize) -> None:
    self.valid = 0
    self.tag = None
    self.block = [None for i in range(blockSize)]

  def attributes(self):
    return (self.valid, self.tag, self.block)

  def update_line(self, tag, offset, data):
    self.valid = True
    self.tag = tag
    self.block = data
