// BFS (a little bit faster)
import collections


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]):
        res = []
        que = collections.deque([[0], ])
        while que:
            base_path = que.popleft()
            if base_path[-1] == len(graph) - 1:
                res.append(base_path)
                continue
            for neighbor in graph[base_path[-1]]:
                new_path = base_path + [neighbor]
                que.append(new_path)
        return res


// DFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        for neighbor in graph[0]:
            self.dfs([0, neighbor], graph, res)
        return res

    def dfs(self, path, graph, res):
        if path[-1] == len(graph) - 1:
            res.append(path)
            return
        for neighbor in graph[path[-1]]:
            self.dfs(path + [neighbor], graph, res)
            
