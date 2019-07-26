class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + [1] * len(flowerbed) + [0]
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                bed[i] = 0
                bed[i+1] = 0
                bed[i+2] = 0
        
        for i in range(1, len(bed) - 1):
            if not bed[i]:
                continue
            bed[i+1] = 0
            n -= 1

        return n <= 0
