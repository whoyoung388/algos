class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        res = []
        for rLength in range(numRows):
            res.append([1] * (rLength+1))
        
        for row in range(2, numRows):
            prev_layer = res[row-1]
            curr_layer = res[row]
            for num in range(1, len(curr_layer)-1):
                curr_layer[num] = prev_layer[num-1] + prev_layer[num]
            res[row] = curr_layer
            
        return res
