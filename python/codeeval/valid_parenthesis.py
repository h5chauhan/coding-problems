from collections import deque
import sys

def main():
  file = open(sys.argv[1],'r')
  for line in file:
    for e in list(line.rstrip()):
      print e
      stack = []
      if e == "[" or e == "(":
        stack.append(e)
      elif e == "]":
        a = stack.pop()
        if e+a != "[]":
          print False
      elif  e == ")":
        a = stack.pop()
        if e+a != "[]":
          print False
    print True

if __name__ == "__main__":
  main()
