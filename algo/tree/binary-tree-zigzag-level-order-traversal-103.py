class Solution(object):
    def zigzagLevelOrder(self, root):
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

        rs = []
        for i in range(len(r)):
            if i % 2 == 0:
                rs.append(r[i])
            else:
                rs.append(list(reversed(r[i])))
        return rs
