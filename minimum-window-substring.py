class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            if (map.containsKey(t.charAt(i))) {
                map.put(t.charAt(i), map.get(t.charAt(i))+1);
            } else {
                map.put(t.charAt(i), 1);
            }
        }
        
        int head = 0, length = Integer.MAX_VALUE;
        int left = 0, right = 0;
        int counts = map.size();
        
        while (right < s.length()) {
            char c = s.charAt(right);
            if (map.containsKey(c)) {
                map.put(c, map.get(c)-1);
                if (map.get(c) == 0) {
                    counts--;
                }
            }
            right++;
            while (counts == 0) {
                char lc = s.charAt(left);
                if (map.containsKey(lc)) {
                    map.put(lc, map.get(lc)+1);
                    if (map.get(lc) > 0) {
                        counts++;
                    }
                }
                if (right - left < length) {
                    head = left;
                    length = right - left;
                }
                left++;
            }
        }
        if (length == Integer.MAX_VALUE) {
            return "";
        }
        return s.substring(head, head + length);
    }
}
