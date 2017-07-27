# This returns the length of longest substring that does not contain repeating character.
# e.g. "abcabcbb" has "abc" with length 3.
# Solution for
def lengthOfLongestSubstring(s):
    i, j, maxLen = 0, 0, 0
    chars = set()

    while (i < len(s) and j < len(s)):
        if s[j] not in chars:
            chars.add(s[j])
            j = j+1
            maxLen = max(maxLen, j - i)
        else:
            chars.remove(s[i])
            i = i + 1
    return maxLen, chars

s = input()
print(lengthOfLongestSubstring(s))
