class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        return self.dfs(nums, [])
    
    def dfs(self, nums, seq):
        if not nums:
            return len(seq)
        l1 = 0
        if seq == [] or nums[0] > seq[-1]:
            l1 = self.dfs(nums[1:], seq + [nums[0]])
        l2 = self.dfs(nums[1:], seq)
        return max(l1, l2)
