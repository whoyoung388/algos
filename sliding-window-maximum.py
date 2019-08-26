# Monotonic Queue, Time: O(2N) = O(N)
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        monoque = deque()
        
        for i in range(len(nums)):
            while monoque and nums[i] > nums[monoque[-1]]:
                monoque.pop()
            monoque.append(i)
            if i >= k - 1:
                res.append(nums[monoque[0]])
            if monoque[0] == i - k + 1:
                monoque.popleft()
        
        return res


# Brute Force, Time: O((N-k+1)*k)
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
