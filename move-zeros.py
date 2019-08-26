class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            nums[i], nums[zero] = nums[zero], nums[i] 
            zero += 1
