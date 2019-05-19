class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int rooms = 0;
        
        int n = intervals.length;
        int[] starts = new int[n];
        int[] ends = new int[n];
        
        for (int i = 0; i < n; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        
        Arrays.sort(starts);
        Arrays.sort(ends);
        
        for (int i = 0, j = 0; i < n; i++) {
            if (starts[i] < ends[j]) {
              rooms++;  
            } else {
                j++;
            }
        }
        
        return rooms;
    }
}
