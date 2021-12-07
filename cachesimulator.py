# File: cachesimulator.py
# Author(s): Adam Sulemanji and Tristan Nigos
# Date: 12/01/2021
# Section: 505 
# E-mail(s): adamsulemanji@tamu.edu tristanigos@tamu.edu
# Description:
# e.g., The content of this file implements main.py file


## Documentation for the cachesimulator.py
#
#
# @file cachesimulator.py
#
# @brief The files defines the methods for the main file and simulating it


## 
# @mainpage CSCE312 Cache Simulator Project
# 
# @section Author Created by: Adam Sulemanji and Tristan Nigos
# @section idfiahd Cache Simulator information
# Click on this to navigate to the cachesimulator.py file
#
#
#
#
#
## @section kalhd Cache Information
# Click on this to navigate to the cache.Cache class
#
## @section kalhdh Set Information
# Click on this to navigate to the set.Set class
#
## @section kalhdk Line Information
# Click on this to navigate to the lines.Line class
#
## @section kjahsd Navigate over the class tab to learn more information about each class and its methods


import cache
import set
import os
import sys


## Documentation for the print menu method
# @param none
# @brief printing out the menu
# @code
# def print_menu():
#   print("*** Cache simulator menu ***",'\n',
#   "type one command:", '\n',
#   "1. cache-read", '\n',
#   "2. cache-write",'\n',
#   "3. cache-flush",'\n',
#   "4. cache-view",'\n',
#   "5. memory-view",'\n',
#   "6. cache-dump",'\n',
#   "7. memory-dump",'\n',
#   "8. quit",'\n',
#   "****************************")
#   print()
# @endcode

def print_menu():
  print("*** Cache simulator menu ***",'\n',
  "type one command:", '\n',
  "1. cache-read", '\n',
  "2. cache-write",'\n',
  "3. cache-flush",'\n',
  "4. cache-view",'\n',
  "5. memory-view",'\n',
  "6. cache-dump",'\n',
  "7. memory-dump",'\n',
  "8. quit",'\n',
  "****************************")
  print()

## Documentation for the main function
# @param none
# @brief Takes in the file for the comand line and intializes the main memory. Takes in a command from the user and does the respecive command until "quit" is entered. 
# @code
# def main():
#
#   c = cache.Cache()
#   c.initialize_memory(sys.argv[1])
#   c.configure_cache()
#
#
#   while True:
#     print_menu()
#     line = input("type one command: ").split()
#   
#     if line[0] == "cache-read":
#       if len(line) != 2:
#         print("invalid number of arguments, try again.")
#       else:
#         c.cache_read(line[1])
#    
#     elif line[0] == "cache-write":
#       if len(line) != 3:
#         print("invalid number of arguments, try again.")
#       else:
#         c.cache_write(line[1], line[2])
#
#     elif line[0] == "cache-flush":
#       c.cache_flush()
#   
#     elif line[0] == "cache-view":
#       c.cache_view()
#    
#     elif line[0] == "memory-view":
#       c.memory_view()
#    
#     elif line[0] == "cache-dump":
#       c.cache_dump()
#    
#     elif line[0] == "memory-dump":
#       c.memory_dump()
#
#     elif line[0] == "quit":
#       break
#
#     else:
#       print("invalid command, try again.")
# @endcode
def main():

  c = cache.Cache()
  c.initialize_memory(sys.argv[1])
  c.configure_cache()


  while True:
    print_menu()
    line = input("type one command: ").split()
    
    if line[0] == "cache-read":
      if len(line) != 2:
        print("invalid number of arguments, try again.")
      else:
        c.cache_read(line[1])
    
    elif line[0] == "cache-write":
      if len(line) != 3:
        print("invalid number of arguments, try again.")
      else:
        c.cache_write(line[1], line[2])

    elif line[0] == "cache-flush":
      c.cache_flush()
    
    elif line[0] == "cache-view":
      c.cache_view()
    
    elif line[0] == "memory-view":
      c.memory_view()
    
    elif line[0] == "cache-dump":
      c.cache_dump()
    
    elif line[0] == "memory-dump":
      c.memory_dump()

    elif line[0] == "quit":
      break

    else:
      print("invalid command, try again.")
main()