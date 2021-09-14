# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        from collections import deque
        result = []
        queue = deque([root])
        
        while len(queue) != 0:
            node = queue.popleft()
            
            if not node:
                continue
            
            queue.append(node.left)
            queue.append(node.right)
            result.append(node.val)
            
        return result
        