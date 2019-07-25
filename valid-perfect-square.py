class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid
            else:
                right = mid
        
        if left**2 == num or right**2 == num:
            return True
        return False
