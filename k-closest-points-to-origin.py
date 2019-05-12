import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []
        for point in points:
            heapq.heappush(distances, (-1 * self.calDist(point), point))
            if len(distances) > K:
                heapq.heappop(distances)
        return [point for dis, point in distances]


    def calDist(self, point):
        x, y = point
        return x**2 + y**2
