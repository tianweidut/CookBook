# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        self.max = -sys.maxint
        self.dfs(root)
        return self.max

    def dfs(self, root):
        if not root:
            return 0

        lmax = self.dfs(root.left)
        rmax = self.dfs(root.right)

        self.max = max(self.max,
                       root.val + max(0, lmax) + max(0, rmax))

        return max(0, lmax, rmax) + root.val
