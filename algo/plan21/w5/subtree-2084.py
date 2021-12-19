class Solution:
    def isSubStructure(self, a: TreeNode, b: TreeNode) -> bool:
        if b is None: return False
        if a is None: return b is None
        return self.is_same(a, b) or self.isSubStructure(a.left, b) or self.isSubStructure(a.right, b)
        
    def is_same(self, a, b):
        if a is None and b is not None: return False
        if b is None: return True
        return a.val == b.val and self.is_same(a.left, b.left) and self.is_same(a.right, b.right)