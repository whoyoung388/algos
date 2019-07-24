class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        cumul = costs[0]
        for n in range(1, len(costs)):
            prev = cumul[:]
            curr = costs[n]
            for i in range(3):
                cumul[i] = min(prev[(i+1) % 3], prev[(i+2) % 3]) + curr[i]
            # cumul = [min(cumul[(i+1) % 3], cumul[(i+2) % 3]) + curr[i] for i in range(3)]
        return min(cumul)
