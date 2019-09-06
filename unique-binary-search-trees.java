class Solution {
    public int numTrees(int n) {
        if (n < 2) {
            return 1;
        }
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            for (int head = 1; head <= i; head++) {
                dp[i] += dp[head-1] * dp[i-head];
            }
        }
        return dp[n];
    }
}
