import sys

def main():
  file = open(sys.argv[1])
  for l in file:
    line = l.rstrip().split(",")
    binary = bin(int(line[0]))
    if binary[-int(line[1])] == binary[-int(line[2])]:
      print("true")
    else:
      print("false")

if __name__=="__main__":
  main()
