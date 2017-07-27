#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#   Example:
#   Input: "babad"
#   Output: "bab"
#   Note: "aba" is also a valid answer.

class Solution(object):
    def longestPalindromicsSubstr(self, s):
        output = ""
        i = 1
        for a in s:
            subStr = a
            for b in s[i:]:
                subStr += b
                print(subStr)
                if Solution.isPalindrome(subStr)  and len(subStr) > len(output):
                    output = subStr
            i = i+1
        return output

    @staticmethod
    def isPalindrome(s):
        if len(s) <= 0:
            return False
        i = 0
        j = len(s) - 1
        while i != j:
            if s[i] != s[j]:
                return False
            return True
        return False


print(Solution().longestPalindromicsSubstr(input()))
