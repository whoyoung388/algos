class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        res = 0
        while mask <= n:
            if mask & n != 0:
                res += 1
            mask = mask << 1
        return res
            
