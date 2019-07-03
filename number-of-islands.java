class Coordinate {
    int x, y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        
        int islands = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    islands++;
                    grid[i][j] = '0';
                    bfs(grid, i, j);
                }
            }
        }
        return islands;
    }
    
    private void bfs(char[][] grid, int x, int y) {
        int[] del_x = {1, 0, -1, 0};
        int[] del_y = {0, 1, 0, -1};
        
        Queue<Coordinate> que = new LinkedList<>();
        que.offer(new Coordinate(x, y));
        
        while (!que.isEmpty()) {
            Coordinate c = que.poll();
            for (int i = 0; i < 4; i++) {
                Coordinate curr_c = new Coordinate(c.x + del_x[i], c.y + del_y[i]);
                if (curr_c.x < 0 || curr_c.x >= grid.length ||
                    curr_c.y < 0 || curr_c.y >= grid[0].length) {
                    continue;
                }
                if (grid[curr_c.x][curr_c.y] == '0') {
                    continue;
                }
                grid[curr_c.x][curr_c.y] = '0';
                que.offer(curr_c);
            }
        }
    }
}
