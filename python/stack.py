import sys


def main():
  file = open(sys.argv[1],'r')
  for l in file:
    stack = l.split()
    out = []
    if len(stack):
      for a in stack:
        out.append(stack.pop())
        if len(stack):
          stack.pop()
      print " ".join(out)


if __name__ == '__main__':
  main()
