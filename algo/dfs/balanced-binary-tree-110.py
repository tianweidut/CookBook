Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        is_balanced, _ = self.heigh_balanced(root)
        return is_balanced

    def heigh_balanced(self, root):
        if not root:
            return True, 0
        elif root.left is None and root.right is None:
            return True, 1
        else:
            bl, hl = self.heigh_balanced(root.left)
            br, hr = self.heigh_balanced(root.right)
            return bl and br and abs(hl - hr) <= 1, max(hl, hr) + 1
