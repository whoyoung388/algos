class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[][] dp = new int[n][n];
        
        dp[0][0] = triangle.get(0).get(0);
        
        for (int row = 1; row < n; row++) {
            dp[row][0] = dp[row-1][0] + triangle.get(row).get(0);
            dp[row][row] = dp[row-1][row-1] + triangle.get(row).get(row); 
        }
        
        for (int row = 2; row < n; row++) {
            for (int col = 1; col < row; col++) {
                dp[row][col] = Math.min(dp[row-1][col-1], dp[row-1][col]) + triangle.get(row).get(col);
            }
        }
        
        
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            res = Math.min(res, dp[n-1][i]);
        }
        return res;
    }
}
