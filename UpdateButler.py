import os

## Simple wrapper around butler.py
## Allows for easy updating of the butler.py script
## Since script development not done directly on Raspberry Pi


if __name__ == '__main__':
  while True:
    exit_val = os.system('python butler.py')
    os.system('wget www.your_web_link.com/butler.py -O butler.py')
    #print "hello"
    if exit_val != 0:
      exit()
