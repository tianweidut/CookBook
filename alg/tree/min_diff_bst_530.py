#coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        import sys
        q = []
        self.mid_order(root, q)
        min_diff = sys.maxint

        for i in range(1, len(q)):
            diff = abs(q[i] - q[i - 1])
            min_diff = min(min_diff, diff)

        return min_diff

    def mid_order(self, root, q):
        if not root:
            return

        self.mid_order(root.left, q)
        q.append(root.val)
        self.mid_order(root.right, q)


def main():
    root = TreeNode(2)
    left = TreeNode(1)
    right = TreeNode(3)
    root.left = left
    root.right = right

    print Solution().getMinimumDifference(root)


def main1():
    root = TreeNode(3)
    left = TreeNode(1)
    right = TreeNode(6)
    root.left = left
    root.right = right

    print Solution().getMinimumDifference(root)


if __name__ == "__main__":
    main()
    main1()
