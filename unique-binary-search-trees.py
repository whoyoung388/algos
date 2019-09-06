class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [1, 1] + [0] * (n-1)
        for i in range(2, n+1):
            for root in range(1, i+1):
                left = dp[root - 1]
                right = dp[i-root]
                dp[i] += left * right
        
        return dp[-1]
