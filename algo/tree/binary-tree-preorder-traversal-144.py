# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.r = []
        self.pre_recursive(root)
        return self.r

    def pre_recursive(self, root):
        if not root:
            return

        self.r.append(root.val)
        self.pre_recursive(root.left)
        self.pre_recursive(root.right)

    def pre_iteratively(self, root):
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if not cur:
                continue

            self.r.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
