"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    def _escape(self, s):
        l = str(len(s))
        return l + "," + s
    
    def _dfs(self, node, seq):
        if not node:
            seq.append(self._escape("#"))
            return
        
        seq.append(self._escape(str(node.val)))
        for child in node.children:
            self._dfs(child, seq)
        seq.append(self._escape("#"))

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        seq = []
        self._dfs(root, seq)
        return "".join(seq)

    def _parse(self, seq):
        parsed = []
        pointer = 0
        charNumber = 0
        while pointer < len(seq):
            if seq[pointer] == ",":
                parsed.append(seq[pointer+1:pointer+1+charNumber])
                pointer += 1 + charNumber
                charNumber = 0
                continue
            charNumber = charNumber * 10 + int(seq[pointer])
            pointer += 1
        return parsed
        
    def _dfs2(self, node, seq):
        if not seq:
            return
        
        while seq:
            val = seq.popleft()
            if val == "#":
                return
            child = Node(int(val), [])
            node.children.append(child)
            self._dfs2(child, seq)
                
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        seq = collections.deque(self._parse(data))
        if seq[0] == "#":
            return
        root = Node(int(seq.popleft()), [])
        self._dfs2(root, seq)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
