
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        from collections import defaultdict, deque
        r = defaultdict(list)
        q = deque([(root, 0)])

        while len(q) > 0:
            cur, level = q.popleft()
            r[level].append(cur.val)

            if cur.left:
                q.append((cur.left, level + 1))

            if cur.right:
                q.append((cur.right, level + 1))
        return [r[i] for i in range(len(r))]
