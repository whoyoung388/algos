class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        dfs(n, res, new ArrayList<Integer>());
        return res;
    }
    
    private void dfs(int n, List<List<String>> res, List<Integer> cols) {
        if (cols.size() == n) {
            res.add(drawBoard(cols));
            return;
        }
        int row = cols.size();
        for (int col = 0; col < n; col++) {
            if (!validMove(cols, col, row)) continue;
            cols.add(col);
            dfs(n, res, cols);
            cols.remove(cols.size() - 1);
        }
    }
    
    private List<String> drawBoard(List<Integer> cols) {
        List<String> board = new ArrayList<>();
        
        for (int i = 0; i < cols.size(); i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < cols.size(); j++) {
                sb.append(j == cols.get(i) ? "Q" : ".");
            }
            board.add(sb.toString());
        }
        return board;
    }
    
    private boolean validMove(List<Integer> cols, int col, int row) {
        for (int r = 0; r < cols.size(); r++) {
            if (cols.get(r) == col) return false;
            if (cols.get(r) + r == col + row) return false;
            if (cols.get(r) - r == col - row) return false;
        }
        return true;
    }
}
