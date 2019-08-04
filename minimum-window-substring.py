class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counter = {char: 0 for char in t}
        for char in t:
            counter[char] += 1
        
        goal = len(counter)
        left, right = 0, 0
        head, length = 0, float('inf')
        
        while right < len(s):
            char = s[right]
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    goal -= 1
            right += 1
            while goal == 0:
                char = s[left]
                if char in counter:
                    counter[char] += 1
                    if counter[char] > 0:
                        goal += 1
                
                if right - left < length:
                    head = left
                    length = right - left
                left += 1
        
        if length == float('inf'):
            return ''
        return s[head:head+length]
