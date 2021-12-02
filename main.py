

import cache
import set
import os
import sys




def main():
  print("Hello World")
  c = cache.Cache()
  c.initialize_memory(sys.argv[1])
  c.memory_view()
  c.configure_cache()
  

  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()
  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()
  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()
  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()
  c.cache_read(input("type one command: ").split()[1])
  c.cache_view()

  # c.cache_view()
  # c.cache_dump()
  # c.cache_flush()
  # c.cache_view()
  
  


main()