class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(res, nums, [])
        return res

    def dfs(self, res, nums, temp):
        if len(nums) == 0:
            res.append(temp)
            return
        
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            self.dfs(res, nums[:i] + nums[i+1:], temp + [num])
