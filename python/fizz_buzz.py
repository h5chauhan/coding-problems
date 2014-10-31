import sys


def main():
  file = open(sys.argv[1],'r')
  for l in file:
    a = l.rstrip().split(' ')
    out = ""
    for i in range(int(a[2])):
      if ((i+1)%int(a[0])) == 0:
        out+="F"
      if ((i+1)%int(a[1])) == 0:
        out+="B"
      elif ((i+1)%int(a[0])) != 0 and  ((i+1)%int(a[0])) != 0:
        out+=str(i+1)
      out+=" "
    print out.rstrip()

if __name__ == "__main__":
  main()
