import collections

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        nodes = set([j for i in seqs for j in i])
        if len(nodes) != len(org):
            return False

        neighbors = {i: [] for i in nodes}
        indegree = {i: 0 for i in nodes}
        for seq in seqs:
            for i, node in enumerate(seq[:-1]):
                indegree[seq[i+1]] += 1
                neighbors[node].append(seq[i+1])
        
        que = collections.deque([i for i in indegree if indegree[i] == 0])
        res = []
        while len(que) == 1:
            node = que.popleft()
            res.append(node)
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    que.append(neighbor)
        return res == org
