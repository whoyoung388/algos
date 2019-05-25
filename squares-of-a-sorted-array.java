class Solution {
    public int[] sortedSquares(int[] A) {
        int[] res = new int[A.length];
        int pnt = A.length - 1;
        
        int left = 0, right = A.length - 1;
        while (left <= right) {
            if (Math.abs(A[left]) > Math.abs(A[right])) {
                res[pnt] = A[left] * A[left];
                left++;
            } else {
                res[pnt] = A[right] * A[right];
                right--;
            }
            pnt--;
        }
        return res;
    }
}
