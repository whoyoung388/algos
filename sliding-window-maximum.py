class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k == 0:
            return []
        
        res = [0] * (len(nums) - k + 1)
        
        for i in range(len(res)):
            res[i] = max(nums[i:i+k])
        return res
