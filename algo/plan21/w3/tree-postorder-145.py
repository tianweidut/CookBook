# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.tlist = []
        self._do_postorder_iter(root)
        return self.tlist
    
    def _do_postorder_recu(self, root):
        if root is None:
            return
        
        self._do_postorder_recu(root.left)
        self._do_postorder_recu(root.right)
        self.tlist.append(root.val)
    
    def _do_postorder_iter(self, root):
        if root is None:
            return
        
        stack = [root]
        while stack:
            n = stack[-1]
            
            while n and n.left:
                if getattr(n, "left_marked", False):
                    break
                    
                n.left_marked = True
                stack.append(n.left)
                n = n.left
                
            n = stack[-1]
            if n.right is not None and not getattr(n, "right_marked", False):
                n.right_marked = True
                stack.append(n.right)
            else:
                stack.pop()
                self.tlist.append(n.val)