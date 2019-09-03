class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return
        
        l = start
        r = end
        
        mid = l + (r - l) // 2
        pivot = nums[mid]
        
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        self.quickSort(nums, start, r)
        self.quickSort(nums, l, end)
        
