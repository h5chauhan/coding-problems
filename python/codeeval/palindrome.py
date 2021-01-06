## Checks if given string is a palindrome
class Solution(object):
    def palindrome(self, s):
        if len(s) <= 0:
            return False
        i = 0
        j = len(s) - 1
        while i != j:
            if s[i] != s[j]:
                return False
            return True
        return False

s = input()
sol = Solution()
print(sol.palindrome(s))
