class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(res, nums, new ArrayList<Integer>(), new boolean[nums.length]);
        return res;
    }
    
    private void dfs(List<List<Integer>> res, int[] nums, List<Integer> temp, boolean[] used) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList<Integer>(temp));
            return;
        }
        
        Set<Integer> seen = new HashSet<Integer>();
        for (int i=0; i<nums.length; i++) {
            if (seen.contains(nums[i])) continue;
            if (used[i]==true) continue;
            seen.add(nums[i]);
            temp.add(nums[i]);
            used[i] = true;
            dfs(res, nums, temp, used);
            used[i] = false;
            temp.remove(temp.size() - 1);
        }
        
    }
}
