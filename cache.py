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

    self.recentIndex = 1
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
      self.ramstart, self.ramend = input().split()[1:]
      self.ramstart, self.ramend = int(self.ramstart[2:], 16), int(self.ramend[2:], 16)
      if (self.ramstart <= self.ramend):
        break
    
    self.memory = self.memory[self.ramstart: self.ramend + 1]
    self.msize = self.ramend - self.ramstart + 1
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
      if self.associativity in [1, 2, 4]: break
      else:
        print("ERROR: invalid associativity")
    
    while True:
      self.replacement = int(input("replacement policy: "))
      if self.replacement in [1,2]: break
      else:
        print("ERROR: invalid replace policy")

    while True:
      self.writehit = int(input("write hit policy: "))
      if self.writehit in [1,2]: break
      else:
        print("ERROR: write hit policy")

    while True:
      self.writemiss = int(input("write miss policy: "))
      if self.writemiss in [1,2]: break
      else:
        print("ERROR: write miss policy")
    
    # S = C / (E * B)
    self.ssize = int(self.csize / (self.bsize * self.associativity))
    # s = log2S
    self.indexbits = int(np.log2(self.ssize))
    # b = log2B
    self.offsetbits = int(np.log2(self.bsize))
    # t = log2M (i.e. m) - (s + b)
    self.tagbits = int(np.log2(self.msize)) - (self.indexbits + self.offsetbits)

    # DELETE WHEN PROJECT COMPLETE
    print("\ncache size", self.csize)
    print("number of sets:", self.ssize)
    print("memory size: ", self.msize)
    print("number of lines in each set", self.associativity)
    print("number of blocks in each line", self.bsize)
    print("tag {}, index {}, offset {}".format(self.tagbits, self.indexbits, self.offsetbits))

    
    print("cache successfully configured!\n")
    
    # defining cache as a list of sets, for each set pass (associativity (number of lines), block size, set index)
    self.cache = [set.Set(self.associativity, self.bsize, i) for i in range (self.ssize)]
  
    # defines the blocks of memory that we would overwrite/push into cache following a cache read miss. refer to notes
    for i in range(0, self.msize, self.bsize):
      self.blocks.append(self.memory[i: i + self.bsize])
      

    # convert the ADDRESS to bits and will point to the location the address DATA will be stored.
    # if there's a read miss, write the address



  # obtaining the bits for tag, index, and offset in hexa, int, int respectively
  def binarySplit(self, address):
    binary = bin(int(address, 16))[2:].zfill(8)
    binary = [binary[0: self.tagbits], binary[self.tagbits: self.tagbits + self.indexbits], binary[self.tagbits + self.indexbits: self.tagbits + self.indexbits + self.offsetbits]]
    taghex = (hex(int(binary[0], 2))[2:]).upper()
    
    converted = [taghex.zfill(2), 0 if len(binary[1]) == 0 else int(binary[1], 2), int(binary[2], 2)]
    return converted



  # finding the memory block of size self.bsize that contains the data in memory.
  def findBlock(self, address): 
    # was initially a longer function but i found a way to condense.
    return self.blocks[int(int(address, 16) / self.bsize)]        



  def replacement_policy(self, address, set, addressTag, rw):
    lines = set.getLines()
    # obtain the block of memory (of size blocksize) for line replacement
    block = self.findBlock(address[2:])
    evictionLine = 0

    ### FIX
    dirty = 0
    if rw == "write":
      if self.writemiss == 2 or self.writemiss == 1 and self.writehit == 2:
        dirty = 1

    if not set.isFull():
      for line in lines:
        lineValid = line.attributes()[1]
        if lineValid == 0:
          print("\tcache miss, tags are not equal but set is not full. found an empty line. fill empty line")
          lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
          break
        else:
          evictionLine += 1

    # invoke specified replacement policy
    elif self.replacement == 1:
      print("\tcache miss. tags are not equal but set is full. no empty lines. invoke replacement policy")
      # invoke random replacement
      evictionLine = random.randint(0, self.associativity - 1)
      print("\tDIRTY {} inputting new block of memory into cache at line index {}, where index used random replacement policy".format(dirty, evictionLine))
      lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
    elif self.replacement == 2:
      print("\tcache miss. tags are not equal but set is full. no empty lines. invoke replacement policy")
      evictionLine, index = 0, 0
      lruIndex = lines[0].attributes()[4]

      for line in lines:
        lineReadIndex = line.attributes()[4]
        if lineReadIndex < lruIndex:
          lruIndex = lineReadIndex
          evictionLine = index
        index += 1
      print("\tinputting new block of memory into cache at line index {}, where index used LRU policy".format(evictionLine))
      lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
      
    return evictionLine

    
  def cache_read(self, address):
    # hexa, int, int
    (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(address)

    # obtaining the set at the set index it should be in
    set = self.cache[addressSetIndex]

    # obtains (x-way associativity) x lines within the specified set
    lines = set.getLines()

    hit = False
    data = None
    evictionLine = 0
    
    for line in lines:
      # hex, hex, list(hex)
      (lineValid, lineTag, lineBlock) = line.attributes()[1:4]

      if lineValid == 1 and lineTag == addressTag:
        # cache hit, obtain data from the cache @ particular set -> index -> offset
        print("cache hit, tags are equal at an appropriate line. read data")
        hit = True
        line.update_line(addressTag, self.findBlock(address[2:]), 0, self.recentIndex)
        data = "0x" + lineBlock[addressBlockOffset]
        address = -1
        evictionLine = -1
        break


    if not hit:
      # cache miss and all lines in specific set are filled. consult policy for replacement
      evictionLine = self.replacement_policy(address, set, addressTag, "read")

      # obtain the data from memory (which will be stored in the cache) indexed by memory address (hexa) converted to binary
      data = "0x" + str(self.memory[int(address, 16)])

    print("set:", addressSetIndex)
    print("tag:", addressTag)
    print("hit:", "yes" if hit else "no")
    print("eviction line:", evictionLine)
    print("ram address:", address)
    print("data:", data, "\n")
    self.recentIndex += 1



  def cache_write(self, address, data):
    # the cache-write command writes data to an address in the cache.
    (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(address)

    # obtaining the set at the set index the address should be in
    set = self.cache[addressSetIndex]

    # obtains (x-way associativity) x lines within the specified set
    lines = set.getLines()

    dirty = 0
    hit = False
    evictionLine = -1
    
    # find the line with bits that correspond to the address bits 
    for line in lines:
      
      (lineValid, lineTag, lineBlock) = line.attributes()[1:4]

      if lineValid == 1 and lineTag == addressTag:
        # cache hit (address is found in the cache line)
        print("cache hit, override data in the cache with requested data.")
        hit = True

        print("dirty bit is set to 1 because not writing to RAM" if self.writehit == 2 else "dirty bit is set to 0 because writing to RAM")
        dirty = 1 if self.writehit == 2 else 0

        # write data to block in cache
        lineBlock[addressBlockOffset] = data[2:]

        # update line's block and dirty bit
        line.update_line(addressTag, lineBlock, dirty, self.recentIndex)

        if self.writehit == 1:
          # write-through, write the data to block in RAM
          print("write through, override data in RAM with data in cache")
          self.memory[int(address, 16)] = data[2:]

          # update block which is underlied by memory
          self.findBlock(address[2:])[addressBlockOffset] = data[2:]
        break
    
    if not hit:
      # cache miss
      print("cache miss, set doesn't contain line containing the address.")     

      if self.writemiss == 2 or self.writemiss == 1 and self.writehit == 2:
        dirty = 1 

      if self.writemiss == 1:
        # write allocate. load data from RAM (before updating) using replacement policy to cache, followed by write hit action 
        print("write allocate. loading block from RAM (before updating data) to cache using replacement")
        evictionLine = self.replacement_policy(address, set, addressTag, "write")

        # write-hit action always writes data to cache
        print("updating the block in cache with new data.")
        lineBlock = lines[evictionLine].attributes()[3]
        lineBlock[addressBlockOffset] = data[2:]
        lines[evictionLine].update_line(addressTag, lineBlock, dirty, self.recentIndex)


      if self.writehit == 1 or self.writemiss == 2:
        # write-allocate miss => write-through hit, write to RAM and block.
        # no-write-allocate miss => write to RAM
        print("writing data to block in RAM")
        self.memory[int(address, 16)] = data[2:]
        # update block which is underlied by memory
        self.findBlock(address[2:])[addressBlockOffset] = data[2:]
      else:
        print("not writing data to RAM, therefore it's dirty")

    print("set:", addressSetIndex)
    print("tag:", addressTag)
    print("hit:", "yes" if hit else "no")
    print("eviction line:", evictionLine)
    print("ram address:", address)
    print("data:", data)
    print("dirty bit:", dirty)
    self.recentIndex += 1


  def cache_view(self):
    print("cache size:",  self.csize)
    print("data block size:", self.bsize)
    print("associativity:", self.associativity)
    print("replacement_policy: {}".format("random_replacement" if self.replacement == 1 else "least_recently_used"))
    print("write_hit_policy: {}".format("write_through" if self.writehit == 1 else "write_back"))
    print("write_miss_policy: {}".format("write_allocate" if self.writemiss == 1 else "write_no_allocate"))

    print("number_of_cache_hits:", self.hits, '\n', 
    "number_of_cache_misses:", self.misses)
    

    print("cache content:")
    for set in self.cache:
      for line in set.getLines():
        attributes = line.attributes()
        vals = attributes[3]
        print(attributes[1], attributes[0], attributes[2], end = " ")
        for val in vals:
          print(val, end = " ")
        print(attributes[4])
  


  def memory_view(self):
    print("memory_size:", self.msize)
    print("memory_content:")
    print("address:data") 
    counter = 0
    while True:
      hexNum = hex(self.ramstart + counter)
      print("{}{}: ".format(hexNum[0:2], hexNum[2:].upper().zfill(2)), end = "")
      vals = self.memory[0 + counter: 8 + counter]
      for h in vals:
        print(h, end = " ")
      print()
      counter += 8

      if counter >= self.msize:
        break



  def cache_flush(self):
    for set in self.cache:
      for line in set.getLines():
        line.flush(self.bsize)
    print("cache_cleared")


  def cache_dump(self):
    for set in self.cache:
      for line in set.getLines():
        attributes = line.attributes()
        for data in attributes[3]:
          print(data, end = " ")
        print()



  def memory_dump(self):
    for data in self.memory:
      print(data)
