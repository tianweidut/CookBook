# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        if root is None:
            return True
        
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            x = queue.popleft()
            y = queue.popleft()
            
            if x is None and y is None:
                continue
            
            if x is None or y is None:
                return False
            
            if x.val != y.val:
                return False
            
            queue.append(x.left)
            queue.append(y.right)
            queue.append(x.right)
            queue.append(y.left)
        
        return True

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def _r(l, r):
            if l is None and r is None:
                return True
            
            if l is None or r is None:
                return False
            
            return l.val == r.val and _r(l.left, r.right) and _r(l.right, r.left)
        
        return _r(root.left, root.right) if root is not None else True