class Solution {
    public int longestPalindrome(String s) {
        Set<Character> set = new HashSet<Character>();
        for (char c : s.toCharArray()) {
            if (set.contains(c)) set.remove(c);
            else set.add(c);
        }
        int remove = set.size();
        if (remove != 0) {
            remove--;
        }
        return s.length() - remove;
    }
}
