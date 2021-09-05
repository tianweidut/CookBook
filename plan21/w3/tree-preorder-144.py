# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.tlist = []
        self._do_preorder_iter(root)
        return self.tlist
    
    def _do_preorder_re(self, root):
        if root is None:
            return
        
        self.tlist.append(root.val)
        self._do_preorder(root.left)
        self._do_preorder(root.right)
        
    def _do_preorder_iter(self, root):        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node is None:
                continue
                
            self.tlist.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
                