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
            
