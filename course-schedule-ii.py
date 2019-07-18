import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):
        res = []
        indegree = [0] * numCourses
        neighbors = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            indegree[dst] += 1
            neighbors[src].append(dst)
        
        queue = collections.deque([i for i, n in enumerate(indegree)if n == 0])
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res if len(res) == numCourses else []
