class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        
        count = 0
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j]:
                    count += 1
        return count
