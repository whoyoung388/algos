// Brute Force, will TLE
class Solution {
    public int lengthOfLIS(int[] nums) {
        return dfs(nums, Integer.MIN_VALUE, 0);
    }
    
    private int dfs(int[] nums, int prev, int curr_indx) {
        if (curr_indx == nums.length) {
            return 0;
        }
        
        int take = 0;
        if (nums[curr_indx] > prev) {
            take = dfs(nums, nums[curr_indx], curr_indx + 1) + 1;
        }
        int notake = dfs(nums, prev, curr_indx + 1);
        return Math.max(take, notake);
    }
}
