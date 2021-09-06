# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        import math
        if root is None:
            return 0
        
        hl = 0
        left = root
        while left:
            hl += 1
            left = left.left
            
        hr = 0
        right = root
        while right:
            hr += 1
            right = right.right
            
        if hl == hr:
            return int(math.pow(2, hl) - 1)
        
	return 1 + self.countNodes(root.left) + self.countNodes(root.right)