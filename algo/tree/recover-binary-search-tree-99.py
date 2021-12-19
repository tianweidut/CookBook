# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Two elements of a binary search tree (BST) are swapped by mistake.
#Recover the tree without changing its structure.
#A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.last = None  # last初始要为空，因为中序遍历的第一个节点并不是根节点
        self.first = None
        self.second = None

        self.dfs(root)

        tmp = self.second.val
        self.second.val = self.first.val
        self.first.val = tmp

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)

        if self.last.val > root.val:
            if self.first is None:
                self.first = self.last
            self.second = root
        self.last = root

        self.dfs(root.right)
