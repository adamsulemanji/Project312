

import cache
import set
import os
import sys

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
  "****************************", end = "\n")


def main():



  

  c = cache.Cache()
  c.initialize_memory(sys.argv[1])

  # val = ""


  # while val != "quit":
  #   val = input("type one command: ")
    
  #   if val == "cache-read":
  #     c.cache_read(input("type one command: ").split()[1])
    
  #   elif val == "cache-write":
      
  # c.memory_view()
  c.configure_cache()
  

  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()
  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()
  data = input("type one command: ").split()
  c.cache_write(data[1], data[2])
  c.cache_view()
  c.memory_view()
  # c.cache_read(input("type one command: ").split()[1])
  # c.cache_view()
  # c.cache_read(input("type one command: ").split()[1])
  # c.cache_view()
  # c.cache_read(input("type one command: ").split()[1])
  # c.cache_view()
  # c.cache_read(input("type one command: ").split()[1])
  # c.cache_view()

  # c.cache_view()
  # c.cache_dump()
  # c.cache_flush()
  # c.cache_view()
  
  


main()