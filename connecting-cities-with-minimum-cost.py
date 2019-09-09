class UnionFind(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return False
        if self.ranks[parent_u] < self.ranks[parent_v]:
            self.parents[parent_u] = parent_v
        elif self.ranks[parent_u] > self.ranks[parent_v]:
            self.parents[parent_v] = parent_u
        else:
            self.parents[parent_u] = parent_v
            self.ranks[parent_v] += 1
        return True


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        graph = UnionFind(N)
        connections.sort(key=lambda x: x[2])
        cost = 0
        for u, v, c in connections:
            if graph.union(u-1, v-1):
                cost += c
        isConnected = len(set([graph.find(n) for n in range(N)])) == 1
        return cost if isConnected else -1
