import sys

def main():
  file = open(sys.argv[1],'r')
  num_line = int(file.readline())
  tup = ()
  for line in file:
    tup = tup + ((len(line.rstrip()),line.rstrip()),)
  tup = tuple(sorted(tup, key=lambda item: item[0], reverse=True))
  for t in tup:
    if num_line != 0:
      print t[1]
      num_line-=1 
if __name__=="__main__":
  main()
