#coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        import sys
        """
        :type root: TreeNode
        :rtype: bool
        """
        max_int = sys.maxint
        return self._validate(root, -max_int, max_int)

    def _validate(self, root, min_v, max_v):
        if not root:
            return True

        l = root.left.val if root.left else root.val - 1
        r = root.right.val if root.right else root.val + 1
        return (l < root.val < r and
                min_v < root.val < max_v and
                self._validate(root.left, min_v, root.val) and
                self._validate(root.right, root.val, max_v))


def main():
    root = TreeNode(2)
    left = TreeNode(1)
    right = TreeNode(3)
    root.left = left
    root.right = right

    print Solution().isValidBST(root)


def main1():
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right

    print Solution().isValidBST(root)


if __name__ == "__main__":
    main()
    main1()
