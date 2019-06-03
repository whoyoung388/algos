// 1ms beats 99% DP Solution
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        int maxWord = 0;
        for (String word : wordDict) {
            maxWord = Math.max(word.length(), maxWord);
        }
        
        for (int end = 1; end <= s.length(); end++) {
            for (int start = end - 1; start >= Math.max(0, end-maxWord); start--) {
                if (dp[start] == false) {
                    continue;
                }
                if (wordDict.contains(s.substring(start, end))) {
                    dp[end] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}


// 2ms beats 96% DP Solution
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        
        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j] == false) {
                    continue;
                }
                if (wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}

// DFS + memoization
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        return dfs(s, wordDict, 0, new Boolean[s.length()]);
    }
    
    private boolean dfs(String s, List<String> wordDict, int start, Boolean[] memo) {
        if (start == s.length()) {
            return true;
        }
        
        if (memo[start] != null) {
            return memo[start];
        }
        
        for (int end = start+1; end <= s.length(); end++) {
            if (wordDict.contains(s.substring(start, end)) && dfs(s, wordDict, end, memo)) {
                return memo[start] = true;
            }
        }
        return memo[start] = false;
    }
}



// TLE Naive Solution
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        return dfs(s, dict, 0);
    }

    private boolean dfs(String s, Set<String> wordDict, int start) {
        if (start == s.length()) {
            return true;
        }
        
        for (int end = start + 1; end <= s.length(); end++) {
            if (wordDict.contains(s.substring(start, end)) && dfs(s, wordDict, end)) {
                return true;
            }
        }
        return false;
    }
}
