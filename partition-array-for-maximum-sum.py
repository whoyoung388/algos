"""
Pseudo code:
dp[i] = maximum sum for array A[0] to A[i-1]
dp[i] = dp[i-j-1] + max(A[i-j], A[i-j+1], ... A[i]) * j for 0 <= j < min(K, i)
return dp[len(A)]

i = 5
j = 0

dp = [0, 1, 30, 45, 54, 0, 0, 0]

"""

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * (len(A) + 1)

        for i in range(1, len(A) + 1):
            currMax = -1
            for j in range(min(K, i)):
                if A[i-j-1] > currMax:
                    currMax = A[i-j-1]
                dp[i] = max(dp[i], dp[i-j-1] + currMax * (j+1))

        return dp[-1]
            
