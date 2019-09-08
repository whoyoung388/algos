# DFS
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        return self.equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def equal(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right, t.right)

# String comparison (faster)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        sflat = []
        tflat = []
        self.flatten(s, sflat)
        self.flatten(t, tflat)
        sString = ",".join(sflat)
        tString = ",".join(tflat)
        
        return tString in sString
        
        
    def flatten(self, root: TreeNode, res: list) -> None:
        if not root:
            res.append("null")
            return
        
        res.append("#" + str(root.val))
        self.flatten(root.left, res)
        self.flatten(root.right, res)
