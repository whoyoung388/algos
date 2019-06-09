class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left + 1 < right) {
            int middle = (left + right) / 2;
            if (nums[middle] > nums[middle - 1]) {
                left = middle;
            } else {
                right = middle;
            }
        }
        return nums[right] > nums[left] ? right : left;
    }
}
