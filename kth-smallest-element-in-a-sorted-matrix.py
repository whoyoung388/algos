import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = []
        
        for i in range(min(k, n)):
            heapq.heappush(pq, (matrix[i][0], i, 0))
        
        while k:
            k -= 1
            val, row, col = heapq.heappop(pq)
            if col < n - 1:
                heapq.heappush(pq, (matrix[row][col+1], row, col+1))
        
        return val
