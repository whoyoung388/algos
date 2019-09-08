class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
    
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if self.bisearch(matrix[i], target) != -1:
                return True
        return False

        
    def bisearch(self, l: list, target: int) -> int:
        left, right = 0, len(l) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if l[mid] < target:
                left = mid
            else:
                right = mid
        
        if l[left] == target:
            return left
        if l[right] == target:
            return right
        return -1
        
            
