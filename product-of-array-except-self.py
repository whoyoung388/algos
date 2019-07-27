class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightpass = [1] + nums[:-1]
        leftpass = nums[1:] + [1]
        for i in range(2, len(nums)):
            rightpass[i] *= rightpass[i-1]
            leftpass[len(nums) - i - 1] *= leftpass[len(nums) - i]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = rightpass[i] * leftpass[i]
        return res
