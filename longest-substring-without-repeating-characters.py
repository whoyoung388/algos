# Optimized
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            char = s[right]
            if char in window:
                left = max(window[char] + 1, left)
            window[char] = right
            right += 1
            res = max(res, right - left)
        return res

# use template from #76
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            right += 1
            
            while window[char] != 1:
                tempchar = s[left]
                window[tempchar] -= 1
                left += 1

            if right - left > res:
                res = right - left
            

        return res

# Brute force (TLE)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if j+1-i == len(set(s[i:j+1])):
                    max_l = max(max_l, j+1-i)
        return max_l
