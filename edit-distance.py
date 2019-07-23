class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1

        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i][j-1]+1,
                               dp[i-1][j]+1,
                               dp[i-1][j-1] + self.diff(word1[i-1], word2[j-1]))

        return dp[m][n]

    def diff(self, char1, char2):
        if char1 == char2:
            return 0
        return 1
