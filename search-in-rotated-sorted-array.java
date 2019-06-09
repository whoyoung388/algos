class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        
        int split = nums[nums.length - 1];
        int left = 0, right = nums.length - 1;
        while (left + 1 < right) {
            int middle = (left + right) / 2;
            if (nums[middle] > split && target <= split) {
                left = middle;
                continue;
            }
            if (nums[middle] <= split && target > split) {
                right = middle;
                continue;
            }
            if (nums[middle] < target) {
                left = middle;
            } else {
                right = middle;
            }
        }
        if (nums[left] == target) {
            return left;
        }
        if (nums[right] == target) {
            return right;
        }
        return -1;
    }
}
