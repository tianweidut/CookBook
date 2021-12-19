class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            if root.left is None:
                return 1 + self.minDepth(root.right)
            elif root.right is None:
                return 1 + self.minDepth(root.left)
            else:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
