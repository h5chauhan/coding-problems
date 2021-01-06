class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mul = 1
        result = 0
        sign = 1 if x > 0 else -1
        x = x * sign
        while x:
            result = (result*10) + (x%10)
            mul *= 10
            x = x / 10
        return result * sign * (result < 2**31)
