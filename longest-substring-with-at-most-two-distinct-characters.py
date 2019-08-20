class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        
        window = {}
        left, right = 0, 0
        longest_s = 0
        goal = 2
        
        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if window[char] == 1:
                goal -= 1
            right += 1
            
            while goal < 0:
                leftchar = s[left]
                window[leftchar] -= 1
                if window[leftchar] == 0:
                    goal += 1
                left += 1
            
            if right - left > longest_s:
                longest_s = right - left

        return longest_s
