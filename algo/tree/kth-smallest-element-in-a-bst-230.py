class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cur_cnt = 1
        self.cur_val = root.val
        self.inorder(root, k)
        return self.cur_val

    def inorder(self, root, k):
        if not root:
            return

        self.inorder(root.left, k)

        if self.cur_cnt == k:
            self.cur_val = root.val
            self.cur_cnt += 1
            return self.cur_val
        elif self.cur_cnt < k:
            self.cur_cnt += 1
        else:
            return self.cur_val

        self.inorder(root.right, k)
