class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                if abs(nums[left] + nums[right] + nums[i] - target) < abs(res - target):
                    res = nums[left] + nums[right] + nums[i]

                if nums[left] + nums[right] + nums[i] == target:
                    return target
                if nums[left] + nums[right] + nums[i] < target:
                    left += 1
                else:
                    right -= 1

        return res
        
