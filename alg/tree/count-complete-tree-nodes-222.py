# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0
        while root:
            l_lvl = self.level(root.left)
            r_lvl = self.level(root.right)

            if l_lvl == r_lvl:
                root = root.right
                cnt += 1 << l_lvl
            elif l_lvl > r_lvl:
                root = root.left
                cnt += 1 << r_lvl
            else:
                raise Exception("wrong complete tree")

        return cnt

    def level(self, root):
        cnt = 0
        while root:
            cnt += 1
            root = root.left

        return cnt
