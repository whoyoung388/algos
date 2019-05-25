class Solution {
    public int[] sortTransformedArray(int[] nums, int a, int b, int c) {
        int[] res = new int[nums.length];
        int left = 0, right = nums.length - 1;
        int pnt = a >= 0 ? nums.length - 1 : 0;

        while (left <= right) {
            if (a >= 0) {
                res[pnt--] = foo(nums[left], a, b, c) >= foo(nums[right], a, b, c) ? foo(nums[left++], a, b, c) : foo(nums[right--], a, b, c);
            } else {
                res[pnt++] = foo(nums[left], a, b, c) <= foo(nums[right], a, b, c) ? foo(nums[left++], a, b, c) : foo(nums[right--], a, b, c);
            }
        }

        return res;
    }
    
    private int foo(int x, int a, int b, int c) {
        return x * x * a + x * b + c;
    }
}
