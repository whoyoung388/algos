class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int sum = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            int diff = prices[i+1] - prices[i];
            if (sum < 0) {
                sum = diff;
            } else {
                sum += diff;
            }
            
            if (sum > profit) {
                profit = sum;
            }
        }
        
        return profit;
    }
}
