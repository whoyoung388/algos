class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        seen = set()
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in mapping and t[i] not in seen:
                mapping[s[i]] = t[i]
                seen.add(t[i])
                continue
            
            if mapping.get(s[i]) != t[i]:
                return False

        return True
