class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1]) ** 2
    
        maxarea = 0
        left, right = 0, len(height) - 1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            if w * h > maxarea:
                maxarea = w * h
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxarea
