"""
Pseudo code:
create dp table -> 1-D array with size of books + 1
dp[i] = minimum height needed for first i books
dp[i] either 1) put in new shelf 2) put in previous shelf

if 1): dp[i] = dp[i-1] + books[i][1]
if 2): dp[i] = max(books[i][1], dp[j]) for j in range(i-1, -1, -1)

return dp[n] where n is the length of books
"""

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        
        dp = [0] * (len(books) + 1)
        dp[0] = 0
        for i in range(1, len(books)+1):
            width = books[i-1][0]
            height = books[i-1][1]
            dp[i] = height + dp[i-1]
            for j in range(i-1, -1, -1):
                width += books[j-1][0]
                height = max(height, books[j-1][1])
                if width > shelf_width:
                    break
                dp[i] = min(dp[j-1] + height, dp[i])
                
        return dp[-1]
