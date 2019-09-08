class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left = [float('inf')] * len(dominoes)
        right = [float('inf')] * len(dominoes)
        
        # right-pass
        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                continue
            if dominoes[i] == 'R':
                right[i] = 0
                continue
            if i > 0 and right[i-1] != float('inf'):
                right[i] = right[i-1] + 1
        
        # left-pass
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == 'R':
                continue
            if dominoes[i] == 'L':
                left[i] = 0
                continue
            if i < len(dominoes)-1 and left[i+1] != float('inf'):
                left[i] = left[i+1] + 1
        
        res = []
        for i in range(len(dominoes)):
            if left[i] == right[i]:
                res.append('.')
                continue
            if left[i] < right[i]:
                res.append('L')
            else:
                res.append('R')
        return ''.join(res)
        
