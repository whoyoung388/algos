from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image

        que = deque([(sr, sc)])
        color = image[sr][sc]
        if color == newColor:
            return image
        
        while que:
            r, c = que.popleft()
            image[r][c] = newColor
            
            for del_r, del_c in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r, new_c = del_r + r, del_c + c
                if self.validDirection(image, new_r, new_c) and \
                    image[new_r][new_c] == color:
                    que.append((new_r, new_c))
        
        return image
    
    
    def validDirection(self, image, r, c):
        return 0 <= r < len(image) and 0 <= c < len(image[0])
