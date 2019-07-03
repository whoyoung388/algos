// DP O(nlogn)
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = Integer.MIN_VALUE;

        int index;
        for (int i = 0; i < nums.length; i++) {
            index = biSearch(dp, nums[i]);
            // System.out.println(index);
            dp[index] = nums[i];
        }
        
        int res = 0;
        for (int num : dp) {
            // System.out.println(num);
            if (num == Integer.MAX_VALUE) {
                break;
            }
            res++;
        }
        return res - 1;
    }
    
    private int biSearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left + 1 < right) {
            int middle = (left + right) / 2;
            if (nums[middle] < target) {
                left = middle;
            } else {
                right = middle;
            }
        }
        return right;
    }
}

// DP O(n^2)
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);

        int res = 1;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            if (dp[i] > res) {
                res = dp[i];
            }
        }
        return res;
    }
}

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
