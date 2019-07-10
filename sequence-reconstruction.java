class Solution {
    public boolean sequenceReconstruction(int[] org, List<List<Integer>> seqs) {
        Set<Integer> set = new HashSet<>();
        for (List<Integer> seq : seqs) {
            for (int i : seq) {
                set.add(i);
            }
        }
        if (org.length != set.size()) {
            return false;
        }
        Map<Integer, List<Integer>> neighbors = new HashMap<>();
        Map<Integer, Integer> indegree = new HashMap<>();
        for (int node : set) {
            neighbors.put(node, new ArrayList<Integer>());
            indegree.put(node, 0);
        }
        
        for (List<Integer> seq : seqs) {
            for (int i = 0; i < seq.size() - 1; i++) {
                neighbors.get(seq.get(i)).add(seq.get(i+1));
                indegree.put(seq.get(i+1), indegree.get(seq.get(i+1)) + 1);
            }
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int node : set) {
            if (indegree.get(node) == 0) {
                queue.offer(node);
            }
        }
        
        int[] res = new int[set.size()];
        int counter = 0;
        while (queue.size() == 1) {
            int node = queue.poll();
            res[counter++] = node;
            for (int neighbor : neighbors.get(node)) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);
                if (indegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        return Arrays.equals(res, org);
    }
}
