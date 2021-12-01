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
    

    #cache hits and misses
    self.hits = 0
    self.miss = 0

  
  def initialize_memory(self, filename):
    print("intialize the RAM:")

    file = open(filename, 'r')
    lines = file.readlines()

    # change: store the hex values instead of binary
    self.memory = [hexLine[:2] for hexLine in lines]

    # checks for number validity
    valid = False
    while not valid:
      bleh, self.ramstart, self.ramend = input().split()
      self.ramstart, self.ramend = int(self.ramstart[2:], 16), int(self.ramend[2:], 16)
      if (self.ramstart <= self.ramend):
        break
    
    
    self.memory = self.memory[self.ramstart: self.ramend + 1]
    print("'''\nmemory size:", len(self.memory), self.memory)
    print(self.ramstart, self.ramend, "\n'''")

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
    
    while True:
      self.replacement = int(input("replacement policy: "))
      if self.replacement in [1,2]:
        break
      else:
        print("ERROR: invalid replace policy")

    while True:
      self.writehit = int(input("write hit policy: "))
      if self.writehit in [1,2]:
        break
      else:
        print("ERROR: write hit policy")

    while True:
      self.writemiss = int(input("write miss policy: "))
      if self.writemiss in [1,2]:
        break
      else:
        print("ERROR: write miss policy")
    
    

    self.ssize = int(self.csize / (self.bsize * self.associativity))
    self.msize = self.ramend - self.ramstart + 1

    # s = log2S
    self.indexbits = int(np.log2(self.ssize))
    # b = log2B
    self.offsetbits = int(np.log2(self.bsize))
    # t = log2M (i.e. m) - (s + b)
    self.tagbits = int(np.log2(self.msize)) - (self.indexbits + self.offsetbits)

    print("\ncache size", self.csize)
    print("number of sets:", self.ssize)
    print("number of lines in each set", self.associativity)
    print("number of blocks in each line", self.bsize)
    print("tag {}, index {}, offset {}".format(self.tagbits, self.indexbits, self.offsetbits))

    
    print("cache successfully configured!")
    
    # defining cache as a list of sets, for each set pass (associativity (number of lines), block size, set index)
    self.cache = [set.Set(self.associativity, self.bsize, i) for i in range (self.ssize)]
  
    # defines the blocks of memory that we would overwrite/push into cache following a cache read miss. refer to notes
    for i in range(0, self.msize, self.bsize):
      self.blocks.append(self.memory[i: i + self.bsize])
      

    # convert the ADDRESS to bits and will point to the location the address DATA will be stored.
    # if there's a read miss, write the address

  # obtaining the bits for tag, index, and offset in hexa, int, int respectively
  def binarySplit(self, addressIndex):
    binary = bin(int(addressIndex, 16))[2:].zfill(8)
    binary = [binary[0: self.tagbits], binary[self.tagbits: self.tagbits + self.indexbits], binary[self.tagbits + self.indexbits: self.tagbits + self.indexbits + self.offsetbits]]
    
    taghex = (hex(int(binary[0], 2))[2:]).upper()
    converted = ["0" if len(taghex) == 1 else "" + taghex, int(binary[1], 2), int(binary[2], 2)]
    return converted

  # finding the memory block of size self.bsize that contains the data in memory.
  def findBlock(self, address):
    # was initially a longer function but i found a way to condense.
    return self.blocks[int(int(address, 16) / self.bsize)]        

    
  def cache_read(self, addressIndex):
    print("bits:", self.tagbits, self.indexbits, self.offsetbits)

    # hexa, int, int
    (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(addressIndex)
    print("address: tag {} set index {} block offset {}".format(addressTag, addressSetIndex, addressBlockOffset))

    # obtaining the set at the set index it should be in
    set = self.cache[addressSetIndex]

    # obtains (x-way associativity) x lines within the specified set
    lines = set.getLines()

    hit = False
    data = None
    evictionLine = -1
    
    for line in lines:
      # hex, hex, list(hex)
      (lineValid, lineDirty, lineTag, lineBlock) = line.attributes()
      print("line: valid {} tag {} block {}".format(lineValid, lineTag, lineBlock))

      if lineValid == 1 and lineTag == addressTag:
        # cache hit, obtain data from the cache @ particular set -> index -> offset
        hit = True
        data = "0x" + lineBlock[addressBlockOffset]
        addressIndex = -1
        break

    if not hit:
      # cache miss, insert into 1st line for associativity = 1, else do replacement policy

      # obtain the data from memory indexed by memory address (hexa) converted to binary
      data = "0x" + str(self.memory[int(addressIndex, 16)])

      # obtain the block of memory (of size blocksize) for line replacement
      block = self.findBlock(addressIndex[2:])

      # invoke specified replacement policy
      if self.replacement == 1:
        # invoke random replacement
        evictionLine = random.randint(0, self.associativity - 1)
      if self.replacement == 2:
        # FIX NEEDED: invoke least recently used policy
        evictionLine = random.randint(0, self.associativity - 1)

      print("inputting new block of memory into cache at line index {}, where index used a certain replacement policy".format(evictionLine))
      lines[evictionLine].update_line(addressTag, addressBlockOffset, block)



    print("set:", addressSetIndex)
    print("tag:", addressTag)
    print("hit:", "yes" if hit else "no")
    print("eviction line:", evictionLine)
    print("ram address:", addressIndex)
    print("data:", data)
  
  def cache_view(self):
    print("cache size:",  self.csize)
    print("data block size:", self.bsize)
    print("associativity:", self.associativity)

    if self.replacement == 1:
      print("replacement policy:random_replacement")
    else:
      print("replacement policy:least_recently_used")

    if self.writehit == 1:
      print("write_hit_policy:write_through")
    else:
      print("write_hit_policy:write_back")
    
    if self.writemiss == 1:
      print("write_miss_policy:write_allocate")
    else:
      print("write_miss_policy:no_write_allocate")

    print("cache content:")
    for set in self.cache:
      for line in set.getLines():
        attributes = line.attributes()
        vals = attributes[3]
        print("1" if attributes[0] else "0", attributes[1], attributes[2], end = " ")
        for val in vals:
          print(val, end = " ")
        print()
  
  def memory_dump(self):
    print("memory_size:", self.msize)
    print("memory_content:")
    print("address:data") 
    counter = 0
    while True:
      if counter > self.msize:
        break
      hexNum = hex(self.ramstart + counter).upper()
      hexNum = "0" if len(hexNum) == 1 else ""
      print(hex(self.ramstart + counter), ":", end = " ", sep = "")
      vals = self.memory[0 + counter: 8 + counter]
      for h in vals:
        print(h, end =" ")
      counter += 8
      print()
      

      
        
        # self.blocks.append(self.memory[i: i + self.bsize])

    # print("replacement policy:", end="")
    # print("random_replacement" if self.replacement == 1 else "least_recently_used")

    
