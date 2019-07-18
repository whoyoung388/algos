// DP O(n^2)
class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        res = 0
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)

            if dp[i] > res:
                res = dp[i]
        return res



// DFS (TLE)
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
