#!/usr/local/bin/python3

def substr_len(s):

    i,j,len = 0, 0, 0
    charSet = set()
    for ch in s:
        if ch not in charSet:
            charSet.add(ch)
            j += 1
            len = max(len, j-i)

        else:
            charSet.remove(ch)
            i += 1
    return len

s = input()
print(substr_len(s))
