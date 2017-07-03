class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        stack = [T1]

        while stack:
            root = stack.pop()
            ret = self._do_chk(root, T2)
            if ret:
                return True
            else:
                stack.append(root.left)
                stack.append(root.right)

        return False
        return self._do_chk(T1, T2)

    def dfs(self, T1):
        pass

    def _do_chk(self, T1, T2):
        if not T2:
            return True

        if T2 and not T1:
            return False

        return (T1.val == T2.val and
                self._do_chk(T1.left, T2.left) and
                self._do_chk(T1.right, T2.right))
