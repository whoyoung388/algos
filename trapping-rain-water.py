# two-pointer solution: Time O(n), Space O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        volumn = 0
        
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    volumn += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    volumn += rightMax - height[right]
                right -= 1
        
        return volumn


# 3-pass solution: Time O(3n), Space O(n)
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
