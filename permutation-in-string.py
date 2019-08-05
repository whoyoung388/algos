class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {char: 0 for char in s1}
        for char in s1:
            counter[char] += 1
        
        left, right = 0, 0
        goal = len(counter)
        
        while right < len(s2):
            char = s2[right]
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    goal -= 1
            
            right += 1
            while goal == 0:
                char = s2[left]
                if char in counter:
                    counter[char] += 1
                    if counter[char] > 0:
                        goal += 1
                if right - left == len(s1):
                    return True
                left += 1
            
        return False
