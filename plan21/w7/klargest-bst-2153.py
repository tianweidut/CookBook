# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root or k < 1:
            return None
        
        self.cnt = 0
        self.kmax = 0
        self.k = k
        self.search(root)
        return self.kmax
        
    def search(self, root):
        if root is None:
            return
        
        self.search(root.right)
        
        self.cnt += 1
        if self.cnt == self.k:
            self.kmax = root.val
            return
        
        self.search(root.left)
        