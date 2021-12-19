# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        
        if key == root.val:
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            ml_node = root.right
            pre_node = root
            
            while ml_node and ml_node.left:
                pre_node = ml_node
                ml_node = ml_node.left
                
            root.val, ml_node.val = ml_node.val, root.val
            
            if root.right is ml_node:
                root.right = ml_node.right
            else:
                pre_node.left = ml_node.right
                
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root