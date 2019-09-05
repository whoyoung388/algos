class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        
        largest = float('-inf')
        for i in range(len(nums)):
            curr = max(curr + nums[i], nums[i])
            if curr > largest:
                largest = curr
        return largest
        
        
