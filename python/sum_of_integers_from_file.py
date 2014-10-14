import sys

def main():
  file = open(sys.argv[1],'r')
  sum = 0
  for f in file:
    sum += int(f.rstrip())
  print sum

if __name__=="__main__":
  main()
