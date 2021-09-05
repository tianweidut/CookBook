# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        import sys
        return self._chk_valid(root, -sys.maxsize, sys.maxsize)
    
    def _chk_valid(self, root, min_v, max_v):
        if root is None:
            return True
        
        return (min_v < root.val < max_v and
                self._chk_valid(root.left, min_v, root.val) and 
                self._chk_valid(root.right, root.val, max_v)
               )
        