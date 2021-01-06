import sys

def main():
  file = open(sys.argv[1])
  for l in file:
    l = l.rstrip()
    strings = l.split(",")
    strings[1] += strings[1]
    print strings[0] in strings[1]

if __name__=="__main__":
  main()
