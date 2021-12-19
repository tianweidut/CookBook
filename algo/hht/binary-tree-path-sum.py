
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths

    def binaryTreePathSum(self, root, target):
        if not root:
            return []

        self.r = []
        self.dfs(root, target, cur_sum=0, cur_nodes=[])
        return self.r

    def dfs(self, root, target, cur_sum, cur_nodes):
        import copy
        cur_nodes = copy.copy(cur_nodes)

        cur_sum += root.val
        cur_nodes.append(root.val)

        if root.left is None and root.right is None:
            if cur_sum == target:
                self.r.append(cur_nodes)

            return

        if root.left:
            self.dfs(root.left, target, cur_sum, cur_nodes)

        if root.right:
            self.dfs(root.right, target, cur_sum, cur_nodes)
