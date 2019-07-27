class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                dp[i][j] = s[i] == s[j] and (i - j < 3 or dp[i-1][j+1])
                if dp[i][j] and i - j + 1 > len(res):
                    res = s[j:i+1]

        return res
