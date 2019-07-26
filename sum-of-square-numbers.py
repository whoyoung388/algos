class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        _set = set()
        for i in range(c+1):
            if i * i > c:
                break
            _set.add(i * i)
            if c - i * i in _set:
                return True
        return False
