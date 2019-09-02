class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = collections.deque()
        
        word = ""
        for i in range(len(s)):
            char = s[i]
            if char == " ":
                if not word:
                    continue
                else:
                    res.appendleft(word)
                    word = ""
            else:
                word += char
        
        if word:
            res.appendleft(word)
        
        out = ""
        for i in range(len(res)):
            if i != len(res) - 1:
                out += res[i] + " "
            else:
                out += res[i]
        return out
        
