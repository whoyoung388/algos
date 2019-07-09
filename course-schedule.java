class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List[] neighbors = new ArrayList[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            neighbors[i] = new ArrayList<Integer>();
        }
        
        for (int[] pre : prerequisites) {
            int in = pre[0];
            int from = pre[1];
            indegree[in]++;
            neighbors[from].add(in);
        }
        
        Queue<Integer> que = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] != 0) continue;
            que.offer(i);
        }
        
        int count = 0;
        while (!que.isEmpty()) {
            int node = que.poll();
            count++;
            for (int i = 0; i < neighbors[node].size(); i++) {
                int curr_index = (int) neighbors[node].get(i);
                indegree[curr_index]--;
                if (indegree[curr_index] == 0) {
                    que.offer(curr_index);
                }
            }
        }
        return count == numCourses;
    }
}
