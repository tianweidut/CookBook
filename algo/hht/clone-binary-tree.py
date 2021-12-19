
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """

    def cloneTree(self, root):
        if not root:
            return None

        croot = TreeNode(root.val)
        croot.left = self.cloneTree(root.left)
        croot.right = self.cloneTree(root.right)

        return croot
