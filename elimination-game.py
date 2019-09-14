class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return n
        
        return 2 * (n//2 - self.lastRemaining(n//2) + 1)