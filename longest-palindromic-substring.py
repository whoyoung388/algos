# Expand from center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps = ""
        for i in range(len(s)):
            ps = self.expandCenter(s, i, i+1)
            ps2 = self.expandCenter(s, i, i)
            if len(ps) > len(lps):
                lps = ps
            if len(ps2) > len(lps):
                lps = ps2
        return lps
    
    def expandCenter(self, s, left, right):
        ps = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ps = s[left:right+1]
            left -= 1
            right += 1
        return ps



# DP
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
