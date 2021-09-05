# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.tlist = []
        self._do_inorder_iter(root)
        return self.tlist
    
    def _do_inorder_recu(self, root):
        if root is None:
            return
        
        self._do_inorder_recu(root.left)
        self.tlist.append(root.val)
        self._do_inorder_recu(root.right)
        
    def _do_inorder_iter(self, root):
        if root is None:
            return
        
        stack = [root]
        while stack:
            n = stack[-1]
            
            while n and n.left:
                if getattr(n.left, "has_recorded", False):
                    break
                    
                stack.append(n.left)
                n = n.left
                
            n = stack.pop()
            n.has_recorded = True
            self.tlist.append(n.val)
            
            if n.right:
                stack.append(n.right)
        