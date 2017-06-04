
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        allsubs = []
        self.dfs(root, sum, 0, allsubs, "")
        return allsubs

    def dfs(self, root, sum, csum, allsubs, sub):
        if not root:
            return
        elif root.left is None and root.right is None:
            csum += root.val
            sub += ' %s' % root.val
            if sum == csum:
                allsubs.append(map(int, sub.strip().split()))
            return
        else:
            csum += root.val
            sub += ' %s' % root.val
            self.dfs(root.left, sum, csum, allsubs, sub)
            self.dfs(root.right, sum, csum, allsubs, sub)
