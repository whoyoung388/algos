import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k:
            return []
        
        pq = []
        for i in range(len(nums2)):
            heapq.heappush(pq, (nums1[0] + nums2[i], 0, i))
        
        res =[]
        while k and pq:
            k -= 1
            val, ptn1, ptn2 = heapq.heappop(pq)
            res.append([nums1[ptn1], nums2[ptn2]])
            if ptn1 == len(nums1) - 1:
                continue
            heapq.heappush(pq, (nums1[ptn1+1] + nums2[ptn2], ptn1 + 1, ptn2))
        
        return res
