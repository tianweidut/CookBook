
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.dfs(root)

    def dfs(self, root):
        if not root:
            return (None, None)
        elif root.left is None and root.right is None:
            return (root, root)
        else:
            lfirst, llast = self.dfs(root.left)
            rfirst, rlast = self.dfs(root.right)

            if root.left and root.right:
                root.right = lfirst
                root.left = None
                llast.left = None
                llast.right = rfirst
                return (root, rlast)
            elif root.left is None:
                root.right = rfirst
                return (root, rlast)
            elif root.right is None:
                root.right = lfirst
                root.left = None
                return (root, llast)
