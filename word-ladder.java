class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>();
        for (String word : wordList) {
            wordSet.add(word);
        }
        
        HashMap<String, Integer> map = new HashMap<>();
        map.put(beginWord, 1);
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        while (!queue.isEmpty()) {
            String word = queue.poll();
            if (word.equals(endWord)) {
                return map.get(word);
            }
            for (String neighbor : getNeighbors(word, wordSet)) {
                if (map.containsKey(neighbor)) {
                    continue;
                }
                map.put(neighbor, map.get(word) + 1);
                queue.offer(neighbor);
            }
        }
        return 0;
    }
    
    private String replace(String word, int index, char c) {
        char[] arr = word.toCharArray();
        arr[index] = c;
        return new String(arr);
    }
    
    private List<String> getNeighbors(String word, Set<String> wordSet) {
        List<String> neighbors = new ArrayList<>();
        for (int i = 0; i < word.length(); i++) {
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == word.charAt(i)) {
                    continue;
                }
                String neighbor = replace(word, i, c);
                if (wordSet.contains(neighbor)) {
                    neighbors.add(neighbor);
                    wordSet.add(neighbor);
                }
            }
        }
        return neighbors;
    }
}
