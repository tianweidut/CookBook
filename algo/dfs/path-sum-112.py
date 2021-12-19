class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        cur_sum = 0
        return self.find_path(root, cur_sum, sum)

    def find_path(self, root, cur_sum, sum):
        if not root:
            return False
        elif root.left is None and root.right is None:
            return cur_sum + root.val == sum
        else:
            cur_sum += root.val
            return self.find_path(root.left, cur_sum, sum) or self.find_path(root.right, cur_sum, sum)
