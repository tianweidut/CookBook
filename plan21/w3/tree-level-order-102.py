# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        root.lvl = 0
        queue = [root]
        lr = [[]]
        
        while queue:
            n = queue.pop(0)
            
            if n.left:
                queue.append(n.left)
                n.left.lvl = n.lvl + 1
                
            if n.right:
                queue.append(n.right)
                n.right.lvl = n.lvl + 1
                
            if len(lr) <= n.lvl:
                lr.append([])
                
            lr[n.lvl].append(n.val)
            
        return lr