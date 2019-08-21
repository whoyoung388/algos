class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volumn = 0
        
        l = len(height)
        left_max = [height[0]] * l
        right_max =[height[-1]] * l
        
        for i in range(1, l):
            left_max[i] = max(left_max[i-1], height[i])
 
        for i in range(l-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        for i in range(l):
            volumn += min(left_max[i], right_max[i]) - height[i]
            
        return volumn
