class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        
        window = {}
        goal = k
        
        left, right = 0, 0
        max_l = 0
        
        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if window[char] == 1:
                goal -= 1
            
            right += 1
            while goal < 0:
                tempchar = s[left]
                window[tempchar] -= 1
                if window[tempchar] == 0:
                    goal += 1
                
                left += 1
            if right - left > max_l:
                max_l = right - left
            
        return max_l
            
        
        
