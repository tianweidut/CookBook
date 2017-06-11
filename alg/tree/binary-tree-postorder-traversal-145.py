# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.r = []
        self.postorder_iter(root)
        return self.r

    def postorder_recursive(self, root):
        if not root:
            return

        self.postorder_recursive(root.left)
        self.postorder_recursive(root.right)
        self.r.append(root.val)

    def postorder_iter(self, root):
        stack = []

        while root or len(stack) > 0:
            if root:
                if root.left is None and root.right is None:
                    self.r.append(root.val)
                    root = None
                else:
                    stack.append(root)
                    p = root.left
                    root.left = None
                    root = p
            else:
                root = stack[-1]
                p = root.right
                root.right = None
                if p:
                    root = p
                else:
                    stack.pop()
