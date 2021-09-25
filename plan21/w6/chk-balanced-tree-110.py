class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        left_d = self.depth(root.left)
        right_d = self.depth(root.right)
        
        return abs(left_d - right_d) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self, root):
        if root is None:
            return 0
        
        return max(self.depth(root.left), self.depth(root.right)) + 1