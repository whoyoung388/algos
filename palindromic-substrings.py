# Manacher O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        dummy = '#'
        newS = dummy
        for char in s:
            newS += char + dummy

        C, R = 0, 0
        lps = [0] * len(newS)
        count = 0
        for i in range(1, len(newS)):
            if i < R:
                mirror_i = 2*C - i
                lps[i] = min(R - i, lps[mirror_i])
            lps[i] = self.expand(newS, i, lps[i])
            count += (lps[i] + 1) // 2
            if i + lps[i] > R:
                C = i
                R = i + lps[i]
        return count
    
    def expand(self, s, i, dis):
        attemp = dis + 1
        while i-attemp >= 0 and i+attemp < len(s) and s[i-attemp] == s[i+attemp]:
            dis = attemp
            attemp += 1
        return dis


# DP O(n^2)
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
