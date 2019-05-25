class Solution {
    public int[][] employeeFreeTime(int[][][] schedule) {
        List<int[]> res = new ArrayList<>();
        
        List<int[]> timeline = new ArrayList<>();
        for (int[][] employee : schedule) {
            for (int[] range : employee) {
                timeline.add(range);
            }
        }
        
        int n = timeline.size();
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = timeline.get(i)[0];
            ends[i] = timeline.get(i)[1];
        }
        
        Arrays.sort(starts);
        Arrays.sort(ends);
        
        for (int i = 0, j = 0; i < n; i++) {
            if (starts[i] > ends[j]) {
                res.add(new int[] {ends[j], starts[i]});
            }
            j = i;
        }
        
        return res.toArray(new int[res.size() - 1][2]);
    }
}
