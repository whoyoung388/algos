class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums,
            new boolean[nums.length],
            res,
            new ArrayList<Integer>());
        return res;
    }
    
    private void dfs(int[] nums, boolean[] used, List<List<Integer>> res, List<Integer> temp) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList(temp));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            
            temp.add(nums[i]);
            used[i] = true;
            
            dfs(nums, used, res, temp);
            
            used[i] = false;
            temp.remove(temp.size() - 1);
        }
    }
}
