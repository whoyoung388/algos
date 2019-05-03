class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        Map<Character, String> table = new HashMap<>();
        Set<String> used = new HashSet<>();
        return patternIsMatch(pattern, str, table, used);
    }
    
    private boolean patternIsMatch(String pattern,
                                   String str, 
                                   Map<Character, String> table,
                                   Set<String> used) {
        if (pattern.length() == 0) {
            return str.length() == 0;
        }
        
        Character c = pattern.charAt(0);
        if (table.containsKey(c)) {
            if (!str.startsWith(table.get(c))) return false;
            return patternIsMatch(pattern.substring(1),
                                  str.substring(table.get(c).length()),
                                  table,
                                  used);
        };
        
        for (int i = 0; i < str.length(); i++) {
            String word = str.substring(0, i + 1);
            if (used.contains(word)) continue;
            
            table.put(c, word);
            used.add(word);
            if (patternIsMatch(pattern.substring(1),
                               str.substring(i + 1),
                               table,
                               used)) {
                return true;
            }
            table.remove(c);
            used.remove(word);
        }
        
        return false;
    }
}
