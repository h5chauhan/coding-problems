import sys


def main():
  file = open(sys.argv[1],'r')
  for l in file:
    if l.strip():
      stack = l.split()
      out = []
      if len(stack):
        for a in range(len(stack)):
          x = stack.pop()
          if a%2 == 0:
            out.append(x)
        print " ".join(out)


if __name__ == '__main__':
  main()
