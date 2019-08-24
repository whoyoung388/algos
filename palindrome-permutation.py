class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = {char: 0 for char in s}
        
        for char in s:
            counter[char] += 1
        
        oddNumber = 1
        for count in counter.values():
            if count % 2 == 1:
                oddNumber -= 1
                if oddNumber < 0:
                    return False
        
        return True
