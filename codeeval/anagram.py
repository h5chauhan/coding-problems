

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    list1 = list(s1)
    list2 =list(s2)
    list1.sort()
    list2.sort()
    for i, a in enumerate(list1):
        if (list2[i] != a):
            return False
    return True
