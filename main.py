

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
  "****************************")
  print()


def main():

  c = cache.Cache()
  c.initialize_memory(sys.argv[1])
  c.configure_cache()


  while True:
    print_menu()
    line = input("type one command: ").split()
    
    if line[0] == "cache-read":
      c.cache_read(line[1])
    
    elif line[0] == "cache-write":
      c.cache_write(line[1], line[2])

    elif line[0] == "cache-flush":
      c.cache_flush()
    
    elif line[0] == "cache-view":
      c.cache_view()
    
    elif line[0] == "memory-view":
      c.memory_view()
    
    elif line[0] == "cache-dump":
      c.cache_dump()
    
    elif line[0] == "memory_dump":
      c.memory_dump()

    elif line[0] == "quit":
      break
  

main()