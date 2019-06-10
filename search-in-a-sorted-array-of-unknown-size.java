class Solution {
    public int search(ArrayReader reader, int target) {
        int left = 0, right = 10;
        
        while (reader.get(right) < target) {
            right *= 2;
        }
        
        while (left + 1 < right) {
            int middle = (left + right) / 2;
            if (reader.get(middle) < target) {
                left = middle;
            } else {
                right = middle;
            }
        }
        if (reader.get(left) == target) {
            return left;
        }
        if (reader.get(right) == target) {
            return right;
        }
        return -1;
    }
}
