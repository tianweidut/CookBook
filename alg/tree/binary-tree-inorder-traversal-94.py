# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.r = []
        self.inorder_iter(root)
        return self.r

    def inorder_recursive(self, root):
        if not root:
            return

        self.inorder_recursive(root.left)
        self.r.append(root.val)
        self.inorder_recursive(root.right)

    def inorder_iter(self, root):
        if not root:
            return

        stack = [root]

        while len(stack) > 0:
            cur = stack[-1]

            while cur.left:
                p = cur.left
                stack.append(p)
                cur.left = None
                cur = p

            self.r.append(cur.val)
            stack.pop()

            if cur.right:
                stack.append(cur.right)

    def inorder_iter_unmodify(self, root):
        stack = []

        while len(stack) > 0 or root:
            if root:
                stack.push(root)
                root = root.left
            else:
                root = stack.pop()
                self.r.append(root.val)
                root = root.right
