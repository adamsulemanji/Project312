import numpy as np
import random
import set

class Cache():

  def __init__(self) -> None:
    print("*** Welcome to the Cache Simulator ***")
    self.cache = list()
    self.memory = list()
    self.blocks = list()

    self.msize = 0
    self.csize = 0
    self.bsize = 0
    self.ssize = 0
    self.associativity = 0 # number of lines, e

    self.indexbits = 0
    self.offsetbits = 0
    self.tagbits = 0

    self.replacement = 0
    self.writehit = 0
    self.writemiss = 0

    
    # maybe?
    self.ramstart = 0
    self.ramend = 0
    

  
  def initialize_memory(self, filename):
    print("intialize the RAM:")

    file = open(filename, 'r')
    lines = file.readlines()

    # memory = [bin(int(hexLine, 16))[2:].zfill(8) for hexLine in lines] TO CONVERT TO BINARY
    self.memory = [hexLine[:2] for hexLine in lines]

    #for hexLine in lines:
    #  binLine = bin(int(hexLine, 16))[2:].zfill(8)
    #  print(binLine)

    # checks for number validity
    valid = False
    while not valid:
      bleh, self.ramstart, self.ramend = input().split()
      self.ramstart, self.ramend = int(self.ramstart[2:], 16), int(self.ramend[2:], 16)
      if (self.ramstart <= self.ramend):
        break
    
    self.msize = self.ramend - self.ramstart + 1
    self.memory = self.memory[self.ramstart: self.ramend + 1]
    print("'''\nmemory size:", len(self.memory), self.memory)
    print(self.ramstart, self.ramend, self.msize, "\n'''")

    print("RAM successfully initialized!\n")
    # take that input, and initialize with ram, memory address 0x00 the data in the address is 08, put that in dictionary/vector (choose the container that outputs in sorted order)


  
  def configure_cache(self):

    print("configure the cache:")

    ### do we have to check if sizes are in powers of 2?
    self.csize = int(input("cache size: "))
    self.bsize = int(input("block size: "))


    while True:
      self.associativity = int(input("associativity: "))
      if self.associativity in [1, 2, 4]:
        break
      else:
        print("ERROR: invalid associativity")
    
    self.replacement = int(input("replacement policy: "))
    self.writehit = int(input("write hit policy: "))
    self.writemiss = int(input("write miss policy: "))
    

    self.ssize = int(self.csize / (self.bsize * self.associativity))
    self.indexbits = int(np.log2(self.ssize))
    self.offsetbits = int(np.log2(self.bsize))
    
    self.tagbits = int(np.log2(self.msize)) - (self.indexbits + self.offsetbits)

    print("\ncache size", self.csize)
    print("number of sets:", self.ssize)
    print("number of lines in each set", self.associativity)
    print("number of blocks in each line", self.bsize)
    print("tag {}, index {}, offset {}".format(self.tagbits, self.indexbits, self.offsetbits))

    
    print("cache successfully configured!")
    # print and take input
    #
    #
    self.cache = [set.Set(self.associativity, self.bsize, i) for i in range (self.ssize)]
  
    for i in range(0, self.msize, self.bsize):
      self.blocks.append(self.memory[i: i + self.bsize])
      

    # convert the ADDRESS to bits and will point to the location the address DATA will be stored.
    # if there's a read miss, write the address

  # obtaining the bits for tag, index, and offset in hexa, int, int respectively
  def binarySplit(self, memIndex):
    binary = bin(int(memIndex, 16))[2:].zfill(8)
    binary = [binary[0: self.tagbits], binary[self.tagbits: self.tagbits + self.indexbits], binary[self.tagbits + self.indexbits: self.tagbits + self.indexbits + self.offsetbits]]
    converted = [(hex(int(binary[0], 2))[2:]).upper(), int(binary[1], 2), int(binary[2], 2)]
    return converted


  def findBlock(self, address):
    # finding the block of size self.bsize that contains the data in memory.
    return self.blocks[int(int(address, 16) / self.bsize)]        

    # iterate through entire memory cache and find each memory index's tag, index, offset bits
    # for address in range(self.msize):
    #   (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(str(hex(address)))

    #   # memory is contiguous, so when first instance of equivalent tag and index is found, 
    #   # the following memory of length self.bsize is the memory block that contains the data in memory.
    #   if addressTag == tag and addressSetIndex == setIndex:
    #     # we found the start of the block
    #     print("START OF BLOCK IS ", address)
        
    #     # store the following memory of length self.bsize into our "block"
    #     for offset in range(self.bsize):
    #       block.append(self.memory[index + offset])
    #     break
    #   else:
    #     index += 1

    
  def cache_read(self, memIndex):
    print("bits:", self.tagbits, self.indexbits, self.offsetbits)

    # hexa, int, int
    (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(memIndex)
    print("address: tag {} set index {} block offset {}".format(addressTag, addressSetIndex, addressBlockOffset))

    # obtaining the set at the set index it should be in
    set = self.cache[addressSetIndex]

    # for x-way associativity
    lines = set.getLines()

    hit = False
    data = None
    evictionLine = -1
    
    for line in lines:
      # hex, hex, list(hex)
      (lineValid, lineTag, lineBlock) = line.attributes()
      print("line: valid {} tag {} block {}".format(lineValid, lineTag, lineBlock))

      if lineValid == 1 and lineTag == addressTag:
        # cache hit, obtain data from the cache @ particular set -> index -> offset
        hit = True
        data = "0x" + lineBlock[addressBlockOffset]
        memIndex = -1
        break

    if not hit:
      # cache miss, insert into 1st line for associativity = 1, else do replacement policy

      # obtain the data from memory indexed by memory address (hexa) converted to binary
      data = "0x" + str(self.memory[int(memIndex, 16)])

      # obtain the block of memory (of size blocksize) for line replacement
      block = self.findBlock(memIndex[2:])

      # invoke replacement policy
      evictionLine = random.randint(0, self.associativity - 1)
      print("inputting new block of memory into cache at random line index {}".format(evictionLine))
      lines[evictionLine].update_line(addressTag, addressBlockOffset, block)



    print("set:", addressSetIndex)
    print("tag:", addressTag)
    print("hit:", "yes" if hit else "no")
    print("eviction line:", evictionLine)
    print("ram address:", memIndex)
    print("data:", data)


  





    



