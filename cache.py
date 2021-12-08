# File: cache.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements cache.py file

## Documentation for the cache.py file
# @file cache.py

import math
import random
import set

## Documentaion for the cache class
# 
#  The class holds all of the class functions for simulating the cache
class Cache():


  ## The constructor holding all of the variables
  # @param self A pointer to itself
  # @code
  # def __init__(self) -> None:
  #   print("*** Welcome to the Cache Simulator ***")
  #   ## Creating a list of information
  #   self.cache = list()
  #   ## List to hold all of the memory
  #   self.memory = list()
  #   ## List to hold all fo the blocks
  #   self.blocks = list()
  #   ## the number of physical address bits
  #   self.msize = 0
  #   ##  Cache size
  #   self.csize = 0
  #   ## block size
  #   self.bsize = 0
  #   ## set size
  #   self.ssize = 0
  #   ## Number of lines per set
  #   self.associativity = 0 
  #   ## The number of index bits
  #   self.indexbits = 0
  #   ## The number of offset bits
  #   self.offsetbits = 0
  #   ## The number of tag bits
  #   self.tagbits = 0
  #   self.recentIndex = 1
  #   ## Replacement policy information
  #   self.replacement = 0
  #   ## Write hit policy
  #   self.writehit = 0
  #   ## write miss policy
  #   self.writemiss = 0
  #   ## The beginning of the RAM
  #   self.ramstart = 0
  #   ## The end of the RAM
  #   self.ramend = 0
  #   ## Number of cache hits
  #   self.hits = 0
  #   ## Number of cache misses
  #   self.misses = 0
  # @endcode
  def __init__(self) -> None:
    print("*** Welcome to the cache simulator ***")
    ## Creating a list of information
    self.cache = list()
    ## List to hold all of the memory
    self.memory = list()
    ## List to hold all fo the blocks
    self.blocks = list()
    ## the number of physical address bits
    self.msize = 0
    ##  Cache size
    self.csize = 0
    ## block size
    self.bsize = 0
    ## set size
    self.ssize = 0
    ## Number of lines per set
    self.associativity = 0 # number of lines, e
    ## The number of index bits
    self.indexbits = 0
    ## The number of offset bits
    self.offsetbits = 0
    ## The number of tag bits
    self.tagbits = 0

    self.recentIndex = 1
    ## Replacement policy information
    self.replacement = 0
    ## Write hit policy
    self.writehit = 0
    ## write miss policy
    self.writemiss = 0
    
    ## The beginning of the RAM
    self.ramstart = 0
    ## The end of the RAM
    self.ramend = 0
    

    ## Number of cache hits
    self.hits = 0
    ## Number of cache misses
    self.misses = 0

  



  ## Documentation for intializing the RAM 
  # opens the file and puts all the information into the memory list
  # @param self A pointer to itself
  # @param filename The file being opened
  # @code
  # def initialize_memory(self, filename):
  #   print("intialize the RAM:")
  #
  #   file = open(filename, 'r')
  #   lines = file.readlines()
  #
  #   # change: store the hex values instead of binary
  #   self.memory = [hexLine[:2] for hexLine in lines]
  #
  #   # checks for number validity
  #   valid = False
  #   while not valid:
  #     self.ramstart, self.ramend = input().split()[1:]
  #     self.ramstart, self.ramend = int(self.ramstart[2:], 16), int(self.ramend[2:], 16)
  #     if (self.ramstart <= self.ramend):
  #       break
  #  
  #   self.memory = self.memory[self.ramstart: self.ramend + 1]
  #   self.msize = self.ramend - self.ramstart + 1
  #   print("RAM successfully initialized!\n")
  # @endcode
  def initialize_memory(self, filename):
    print("initialize the RAM:")

    file = open(filename, 'r')

    self.memory = ["00" for i in range(256)]

    # checks for number validity
    valid = False
    while not valid:
      self.ramstart, self.ramend = input().split()[1:]
      self.ramstart, self.ramend = int(self.ramstart[2:], 16), int(self.ramend[2:], 16)
      if (self.ramstart <= self.ramend):
        break
    
    self.msize = self.ramend - self.ramstart + 1
    for i in range(self.msize):
      line = file.readline()[:2]
      self.memory[i] = line
    # self.memory = self.memory[self.ramstart: self.ramend + 1]
    
    # print("MEMORY", self.memory)
    
    print("RAM successfully initialized!")





  ## Configuring the cache, takes in inputs from the user to configure cache
  # @param self A pointer to itself
  # @code
  # def configure_cache(self):
  #
  #   print("configure the cache:")
  #
  #   # do we have to check if sizes are in powers of 2?
  #   self.csize = int(input("cache size: "))
  #
  #   while True:
  #     self.bsize = int(input("block size: "))
  #     if self.bsize < self.csize: break
  #     else:
  #       print("ERROR: invalid block size")
  #
  #   while True:
  #     self.associativity = int(input("associativity: "))
  #     if self.associativity in [1, 2, 4]: break
  #     else:
  #       print("ERROR: invalid associativity")
  #
  #   while True:
  #     self.replacement = int(input("replacement policy: "))
  #     if self.replacement in [1,2]: break
  #     else:
  #       print("ERROR: invalid replacement policy")
  #
  #   while True:
  #     self.writehit = int(input("write hit policy: "))
  #     if self.writehit in [1,2]: break
  #     else:
  #       print("ERROR: invalid write hit policy")
  #
  #   while True:
  #     self.writemiss = int(input("write miss policy: "))
  #     if self.writemiss in [1,2]: break
  #     else:
  #       print("ERROR: invalid write miss policy")
  # 
  #   # S = C / (E * B)
  #   self.ssize = int(self.csize / (self.bsize * self.associativity))
  #   # s = log2S
  #   self.indexbits = int(np.log2(self.ssize))
  #   # b = log2B
  #   self.offsetbits = int(np.log2(self.bsize))
  #   # t = log2M (i.e. m) - (s + b)
  #   self.tagbits = int(np.log2(self.msize)) - (self.indexbits + self.offsetbits)
  # 
  #   print("cache successfully configured!\n")
  #
  #   # defining cache as a list of sets, for each set pass (associativity (number of lines), block size, set index)
  #   self.cache = [set.Set(self.associativity, self.bsize, i) for i in range (self.ssize)]
  #
  #   # defines the blocks of memory that we would overwrite/push into cache following a cache read miss. refer to notes
  #   for i in range(0, self.msize, self.bsize):
  #     self.blocks.append(self.memory[i: i + self.bsize])
  # @endcode
  def configure_cache(self):

    print("configure the cache:")

    # do we have to check if sizes are in powers of 2?
    self.csize = int(input("cache size: "))

    while True:
      self.bsize = int(input("data block size: "))
      if self.bsize <= self.csize: break
      else:
        print("ERROR: invalid block size")

    while True:
      self.associativity = int(input("associativity: "))
      if self.associativity in [1, 2, 4]: break
      else:
        print("ERROR: invalid associativity")
    
    while True:
      self.replacement = int(input("replacement policy: "))
      if self.replacement in [1,2]: break
      else:
        print("ERROR: invalid replacement policy")

    while True:
      self.writehit = int(input("write hit policy: "))
      if self.writehit in [1,2]: break
      else:
        print("ERROR: invalid write hit policy")

    while True:
      self.writemiss = int(input("write miss policy: "))
      if self.writemiss in [1,2]: break
      else:
        print("ERROR: invalid write miss policy")
    
    # S = C / (E * B)
    self.ssize = int(self.csize / (self.bsize * self.associativity))
    # s = log2S
    self.indexbits = int(math.log2(self.ssize))
    # b = log2B
    self.offsetbits = int(math.log2(self.bsize))
    # t = log2M (i.e. m) - (s + b)
    self.tagbits = int(math.log2(256)) - (self.indexbits + self.offsetbits)
    
    print("cache successfully configured!")
    
    # defining cache as a list of sets, for each set pass (associativity (number of lines), block size, set index)
    self.cache = [set.Set(self.associativity, self.bsize, i) for i in range (self.ssize)]
  
    # defines the blocks of memory that we would overwrite/push into cache following a cache read miss. refer to notes
    for i in range(0, 256, self.bsize):
      self.blocks.append(self.memory[i: i + self.bsize])
    # print("BLOCKS = ", self.blocks)


  ## Documenting the binary split function
  # @param self A pointer to itself
  # @param address The adderss to get tag, offset and index bits at
  # @retval converted combined bit
  # @code
  # def binarySplit(self, address):
  #   binary = bin(int(address, 16))[2:].zfill(8)
  #   binary = [binary[0: self.tagbits], binary[self.tagbits: self.tagbits + self.indexbits], binary[self.tagbits + self.indexbits: self.tagbits + self.indexbits + self.offsetbits]]
  #   taghex = (hex(int(binary[0], 2))[2:]).upper()
    
  #   converted = [taghex.zfill(2), 0 if len(binary[1]) == 0 else int(binary[1], 2), int(binary[2], 2)]
  #   return converted
  # @endcode
  # obtaining the bits for tag, index, and offset in hexa, int, int respectively
  def binarySplit(self, address):
    binary = bin(int(address, 16))[2:].zfill(8)
    binary = [binary[0: self.tagbits], binary[self.tagbits: self.tagbits + self.indexbits], binary[self.tagbits + self.indexbits: self.tagbits + self.indexbits + self.offsetbits]]
    taghex = (hex(int(binary[0], 2))[2:]).upper()
    # print("bits: tag {} index {} offset {}".format(self.tagbits, self.indexbits, self.offsetbits))
    converted = [taghex.zfill(2), 0 if len(binary[1]) == 0 else int(binary[1], 2), int(binary[2], 2)]
    return converted


  ## Documentation for find a block that contains the data
  # @param self A pointer to itself
  # @param address the address of the data
  # @retval the block that contains the data
  # @code
  # def findBlock(self, address): 
  #   # was initially a longer function but i found a way to condense.
  #   return self.blocks[int(int(address, 16) / self.bsize)]        
  # @endcode
  def findBlock(self, address): 
    # was initially a longer function but i found a way to condense.
    return self.blocks[int(int(address, 16) / self.bsize)]        


  ## Documentation for the replacement policy
  # @param self A pointer to itself
  # @param address the address of the data
  # @param the set the data is in
  # @param addressTag the tag of the address
  # @param Whether the address has been modified
  # @retval evictionLine the line which got evicted
  # @code
  # def replacement_policy(self, address, set, addressTag, dirty):
  #   lines = set.getLines()
  #   # obtain the block of memory (of size blocksize) for line replacement
  #   block = self.findBlock(address[2:])
  #   evictionLine = 0
  #
  #   if not set.isFull():
  #     for line in lines:
  #       lineValid = line.attributes()[1]
  #       if lineValid == 0:
  #         print("\tcache miss, tags are not equal but set is not full. found an empty line. fill empty line")
  #         lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
  #         break
  #       else:
  #         evictionLine += 1
  #
  #   # invoke specified replacement policy
  #   elif self.replacement == 1:
  #     print("\tcache miss. tags are not equal but set is full. no empty lines. invoke replacement policy")
  #     # invoke random replacement
  #     evictionLine = random.randint(0, self.associativity - 1)
  #     print("\tDIRTY {} inputting new block of memory into cache at line index {}, where index used random replacement policy".format(dirty, evictionLine))
  #     lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
  #   elif self.replacement == 2:
  #     print("\tcache miss. tags are not equal but set is full. no empty lines. invoke replacement policy")
  #     evictionLine, index = 0, 0
  #     lruIndex = lines[0].attributes()[4]
  #
  #     for line in lines:
  #       lineReadIndex = line.attributes()[4]
  #       if lineReadIndex < lruIndex:
  #         lruIndex = lineReadIndex
  #         evictionLine = index
  #       index += 1
  #     print("\tinputting new block of memory into cache at line index {}, where index used LRU policy".format(evictionLine))
  #     lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
  #   
  #   return evictionLine
  # @endcode
  def replacement_policy(self, address, set, addressTag, dirty):
    lines = set.getLines()
    # obtain the block of memory (of size blocksize) for line replacement
    block = self.findBlock(address[2:])
    evictionLine = 0

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

      if (lines[evictionLine].attributes()[0] == 1):
        # if the line to evict is dirty, write to RAM and then the blocks.
        # use the set index that we are evicting, as well as the tag of the line to evict. gives us the address
        (tag, setIndex, blockOffset) = self.binarySplit(address)
        setIndexBinary = bin(setIndex)[2:]
        tagBinary = bin(int(lines[evictionLine].attributes()[2], 16))[2:]

        evictLineBinary = '{:<08d}'.format(int(tagBinary + setIndexBinary)[2:])
        print(evictLineBinary, int(evictLineBinary, 16))

        print()

      # print("\tDIRTY {} inputting new block of memory into cache at line index {}, where index used random replacement policy".format(dirty, evictionLine))
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

      if (lines[evictionLine].attributes()[0] == 1):
        # if the line to evict is dirty, write to RAM and then the blocks.
        # use the set index that we are evicting, as well as the tag of the line to evict. gives us the address
        (tag, setIndex, blockOffset) = self.binarySplit(address)
        setIndexBinary = bin(setIndex)[2:]
        tagBinary = bin(int(lines[evictionLine].attributes()[2], 16))[2:]

        evictLineBinary = '0b{:<08d}'.format(int(tagBinary + setIndexBinary))
        print(evictLineBinary, hex(int(evictLineBinary, 2)))
        print(self.findBlock(hex(int(evictLineBinary, 2))))
        print()
      # print("\tinputting new block of memory into cache at line index {}, where index used LRU policy".format(evictionLine))
      lines[evictionLine].update_line(addressTag, block, dirty, self.recentIndex)
      
    return evictionLine

  ## Documentation for reading the cache
  # @param self A pointer to itself
  # @param address the address at which the data is stored at
  # @code
  # def cache_read(self, address):
  #   # hexa, int, int
  #   (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(address)
  #
  #   # obtaining the set at the set index it should be in
  #   set = self.cache[addressSetIndex]
  #
    # obtains (x-way associativity) x lines within the specified set
  #   lines = set.getLines()
  #
  #   hit = False
  #   data = None
  #   evictionLine = 0
  # 
  #   for line in lines:
  #     # hex, hex, list(hex)
  #     (lineValid, lineTag, lineBlock) = line.attributes()[1:4]
  #
  #     if lineValid == 1 and lineTag == addressTag:
  #       # cache hit, obtain data from the cache @ particular set -> index -> offset
  #       print("cache hit, tags are equal at an appropriate line. read data")
  #       self.hits += 1
  #       hit = True
  #       line.update_line(addressTag, self.findBlock(address[2:]), 0, self.recentIndex)
  #       data = "0x" + lineBlock[addressBlockOffset]
  #       address = -1
  #       evictionLine = -1
  #       break
  #
  #
  #   if not hit:
  #     self.misses += 1
  #     # cache miss and all lines in specific set are filled. consult policy for replacement
  #     evictionLine = self.replacement_policy(address, set, addressTag, 0)
  #
  #     # obtain the data from memory (which will be stored in the cache) indexed by memory address (hexa) converted to binary
  #     data = "0x" + str(self.memory[int(address, 16)])
  #
  #   self.hitmiss_print([addressSetIndex, addressTag, hit, evictionLine, address, data])
  #
  #   self.recentIndex += 1
  # @endcode
  def cache_read(self, address):
    # print(int(address[2:], 16), self.msize)
    # if (int(address[2:], 16) > self.msize):
    #   print("ERROR: reading out of range of memory initialization")
    #   return

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
        # print("cache hit, tags are equal at an appropriate line. read data")
        self.hits += 1
        hit = True
        line.update_line(addressTag, self.findBlock(address[2:]), 0, self.recentIndex)
        data = "0x" + lineBlock[addressBlockOffset]
        address = -1
        evictionLine = -1
        break


    if not hit:
      self.misses += 1

      # cache miss and all lines in specific set are filled. consult policy for replacement
      evictionLine = self.replacement_policy(address, set, addressTag, 0)

      # obtain the data from memory (which will be stored in the cache) indexed by memory address (hexa) converted to binary
      data = "0x" + str(self.memory[int(address, 16)])

    self.hitmiss_print([addressSetIndex, addressTag, hit, evictionLine, address, data])
    
    self.recentIndex += 1
  


  ##Documentation for the hit and miss printing method
  # @param self A pointer to itself
  # @param array An array of information to print from cache-read
  # @code
  # def hitmiss_print(self, array):
  #   print("set:", array[0])
  #   print("tag:", array[1])
  #   print("hit:", "yes" if array[2] else "no")
  #   print("eviction line:", array[3])
  #   print("ram address:", array[4])
  #   print("data:", array[5])
  #   print("dirty bit: {}".format(array[6]) if len(array) == 7 else "")
  # @endcode
  def hitmiss_print(self, array):
    print("set:", array[0], sep="")
    print("tag:", array[1], sep="")
    print("hit:", "yes" if array[2] else "no", sep="")
    print("eviction line:", array[3], sep="")
    print("ram address:", array[4], sep="")
    print("data:", array[5], sep="")
    if (len(array) == 7):
      print("dirty bit:{}".format(array[6]))
    
  ## Documentation for the cache write
  # @param self A pointer to itself
  # @param address The address of where to write too
  # @param data the data to to write into the cache
  # @code
  # def cache_write(self, address, data):
  #   # the cache-write command writes data to an address in the cache.
  #   (addressTag, addressSetIndex, addressBlockOffset) = self.binarySplit(address)
  #
  #   # obtaining the set at the set index the address should be in
  #   set = self.cache[addressSetIndex]
  #
  #   # obtains (x-way associativity) x lines within the specified set
  #   lines = set.getLines()
  #
  #   dirty = 0
  #   hit = False
  #   evictionLine = -1
  #
  #   # find the line with bits that correspond to the address bits 
  #   for line in lines:
  #   
  #     (lineValid, lineTag, lineBlock) = line.attributes()[1:4]
  #
  #     if lineValid == 1 and lineTag == addressTag:
  #       # cache hit (address is found in the cache line)
  #       print("cache hit, override data in the cache with requested data.")
  #       hit = True
  #       self.hits += 1
  #
  #       print("dirty bit is set to 1 because not writing to RAM" if self.writehit == 2 else "dirty bit is set to 0 because writing to RAM")
  #       dirty = 1 if self.writehit == 2 else 0
  #
  #       # write data to block in cache
  #       lineBlock[addressBlockOffset] = data[2:]
  #
        # # update line's block and dirty bit
        # line.update_line(addressTag, lineBlock, dirty, self.recentIndex)
        #
        # if self.writehit == 1:
        #   # write-through, write the data to block in RAM
        #   print("write through, override data in RAM with data in cache")
        #   self.memory[int(address, 16)] = data[2:]
        #
        #   # update block which is underlied by memory
        #   self.findBlock(address[2:])[addressBlockOffset] = data[2:]
        # break
  #
  #   if not hit:
  #     # cache miss
  #     print("cache miss, set doesn't contain line containing the address.")     
  #     self.misses += 1
  #
  #     dirty = 1 if self.writemiss == 1 and self.writehit == 2 else 0
  #
  #     if self.writemiss == 1:
  #       # write allocate. load data from RAM (before updating) using replacement policy to cache, followed by write hit action 
  #       print("write allocate. loading block from RAM (before updating data) to cache using replacement")
  #       evictionLine = self.replacement_policy(address, set, addressTag, dirty)
  #
  #       # following a write-allocate miss, write-hit action always writes data to cache
  #       print("updating the block in cache with new data.")
  #       lineBlock = lines[evictionLine].attributes()[3]
  #       lineBlock[addressBlockOffset] = data[2:]
  #       lines[evictionLine].update_line(addressTag, lineBlock, dirty, self.recentIndex)
  #
  #
  #     if self.writehit == 1 or self.writemiss == 2:
  #       # write-allocate miss => write-through hit, write to RAM and block. no-write-allocate miss => write to RAM
  #       print("writing data to block in RAM")
  #       self.memory[int(address, 16)] = data[2:]
  #       # update block which is underlied by memory
  #       self.findBlock(address[2:])[addressBlockOffset] = data[2:]
  #     else:
  #       print("not writing data to RAM, therefore it's dirty")
  #
  #   self.hitmiss_print([addressSetIndex, addressTag, hit, evictionLine, address, data, dirty])
  #   self.recentIndex += 1
  # @endcode
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
        # print("cache hit, override data in the cache with requested data.")
        hit = True
        self.hits += 1

        # print("dirty bit is set to 1 because not writing to RAM" if self.writehit == 2 else "dirty bit is set to 0 because writing to RAM")
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
      self.misses += 1

      dirty = 1 if self.writemiss == 1 and self.writehit == 2 else 0

      if self.writemiss == 1:
        # write allocate. load data from RAM (before updating) using replacement policy to cache, followed by write hit action 
        print("write allocate. loading block from RAM (before updating data) to cache using replacement")
        evictionLine = self.replacement_policy(address, set, addressTag, dirty)

        # following a write-allocate miss, write-hit action always writes data to cache
        print("updating the block in cache with new data.")
        lineBlock = lines[evictionLine].attributes()[3]
        lineBlock[addressBlockOffset] = data[2:]
        lines[evictionLine].update_line(addressTag, lineBlock, dirty, self.recentIndex)


      if self.writehit == 1 or self.writemiss == 2:
        # write-allocate miss => write-through hit, write to RAM and block. no-write-allocate miss => write to RAM
        print("writing data to block in RAM")
        self.memory[int(address, 16)] = data[2:]
        # update block which is underlied by memory
        self.findBlock(address[2:])[addressBlockOffset] = data[2:]
      else:
        print("not writing data to RAM, therefore it's dirty")

    self.hitmiss_print([addressSetIndex, addressTag, hit, evictionLine, address, data, dirty])
    self.recentIndex += 1


  ## Documenation for viewing the curent state of the cache
  # @param self A pointer to itself
  # @code
  # def cache_view(self):
  #   print("cache size:",  self.csize)
  #   print("data block size:", self.bsize)
  #   print("associativity:", self.associativity)
  #   print("replacement_policy: {}".format("random_replacement" if self.replacement == 1 else "least_recently_used"))
  #   print("write_hit_policy: {}".format("write_through" if self.writehit == 1 else "write_back"))
  #   print("write_miss_policy: {}".format("write_allocate" if self.writemiss == 1 else "write_no_allocate"))
  #   print("number_of_cache_hits:", self.hits, "\nnumber_of_cache_misses:", self.misses)
      # print("cache content:")
      #   for set in self.cache:
      #     for line in set.getLines():
      #       attributes = line.attributes()
      #       vals = attributes[3]
      #       print(attributes[1], attributes[0], attributes[2], end = " ")
      #       for val in vals:
      #         print(val, end = " ")
      #       print()
  # @endcode
  def cache_view(self):
    print("cache_size:",  self.csize, sep="")
    print("data_block_size:", self.bsize, sep="")
    print("associativity:", self.associativity, sep="")
    print("replacement_policy:{}".format("random_replacement" if self.replacement == 1 else "least_recently_used"))
    print("write_hit_policy:{}".format("write_through" if self.writehit == 1 else "write_back"))
    print("write_miss_policy:{}".format("write_allocate" if self.writemiss == 1 else "write_no_allocate"))
    print("number_of_cache_hits:", self.hits, sep="")
    print("number_of_cache_misses:", self.misses, sep="")
    

    print("cache_content:")
    for set in self.cache:
      for line in set.getLines():
        attributes = line.attributes()
        vals = attributes[3]
        print(attributes[1], attributes[0], attributes[2], end = " ")
        for val in vals:
          print(val, end = " ")
        print()
        # print(attributes[4])
  

  ## Documentaion for the viewing the current state of the memory
  # @param self A pointer to itself
  # @code
  # def memory_view(self):
  #   print("memory_size:", self.msize)
  #   print("memory_content:")
  #   print("address:data") 
  #   counter = 0
  #   while True:
  #     hexNum = hex(self.ramstart + counter)
  #     print("{}{}: ".format(hexNum[0:2], hexNum[2:].upper().zfill(2)), end = "")
  #     vals = self.memory[0 + counter: 8 + counter]
  #     for h in vals:
  #       print(h, end = " ")
  #     print()
  #     counter += 8
  #
  #     if counter >= self.msize:
  #       break
  # @endcode
  def memory_view(self):
    print("memory_size:", self.msize)
    print("memory_content:")
    print("address:data") 
    counter = 0
    while True:
      hexNum = hex(self.ramstart + counter)
      print("{}{}:".format(hexNum[0:2], hexNum[2:].upper().zfill(2)), end = "")
      vals = self.memory[0 + counter: 8 + counter]
      for h in vals:
        print(h, end = " ")
      print()
      counter += 8

      if counter >= 256:
        break


  ## Documentation for the cache-flush method
  # @param self A pointer to itself
  # @code
  # def cache_flush(self):
  #   for set in self.cache:
  #     for line in set.getLines():
  #       line.flush(self.bsize)
  #   print("cache_cleared")
  # @endcode
  def cache_flush(self):
    for set in self.cache:
      for line in set.getLines():
        line.flush(self.bsize)
    print("cache_cleared")


  ## Documenation for the cache-dump method
  # Getting all information from the cache and dumping it into cache.txt
  # @param self A pointer to itself
  # @code
  # def cache_dump(self):
  #   with open ("cache.txt", "w+") as file:]
  #     for set in self.cache:
  #       for line in set.getLines():
  #         attributes = line.attributes()
  #         for data in attributes[3]:
  #           file.write(data)
  #           file.write(" ")
  #         #   print(data, end = " ")
  #         file.write('\n')
  # @endcode
  def cache_dump(self):
    with open ("cache.txt", "w+") as file:
      for set in self.cache:
        for line in set.getLines():
          attributes = line.attributes()
          for data in attributes[3]:
            file.write(data)
            file.write(" ")
          file.write('\n')


  ## Documentation for the memory-dump method
  # Getting all information memory and dumping into ram.txt
  # @param A pointer to itself
  # @code
  # def memory_dump(self):
  #   with open("ram.txt", "w+") as file:
  #     file.truncate(0)
  #     for data in self.memory:
  #       file.write(data)
  #       file.write('\n')
  # @endcode
  def memory_dump(self):
    with open("ram.txt", "w+") as file:
      file.truncate(0)
      for data in self.memory:
        file.write(data)
        file.write('\n')
