# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        node_l, node_r = root.left, root.right
        root.left = self.mirrorTree(node_r)
        root.right = self.mirrorTree(node_l)
        return root