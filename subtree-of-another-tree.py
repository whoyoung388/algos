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
