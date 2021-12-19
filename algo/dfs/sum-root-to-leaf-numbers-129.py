class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.totalsum = 0
        self.dfs(root, "")
        return self.totalsum

    def dfs(self, root, sub):
        if not root:
            return
        elif root.left is None and root.right is None:
            sub += str(root.val)
            self.totalsum += int(sub)
        else:
            sub += str(root.val)
            self.dfs(root.left, sub)
            self.dfs(root.right, sub)
