# Manacher O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dummy = '#'
        newS = dummy
        for char in s:
            newS += char + dummy
        
        lps = [0] * len(newS)
        C, R = 0, 0
        curr_lps = 0
        curr_c = 0
        for i in range(1, len(newS)):
            if i < R:
                mirror_i = 2*C - i
                lps[i] = min(R-i, lps[mirror_i])
            lps[i] = self.expand(newS, i, lps[i])
            if i + lps[i] > R:
                C = i
                R = i + lps[i]
            if lps[i] > curr_lps:
                curr_lps = lps[i]
                curr_c = i
        res = ""
        for char in newS[curr_c-curr_lps:curr_c+curr_lps+1]:
            if char == dummy:
                continue
            res += char
        return res
        

    def expand(self, s, i, dis) -> int:
        temp = dis + 1
        while i - temp >= 0 and i + temp < len(s) and s[i-temp] == s[i+temp]:
            dis = temp
            temp += 1
        return dis


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
