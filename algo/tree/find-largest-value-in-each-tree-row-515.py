#coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        from Queue import Queue

        row_map = {}

        q = Queue()
        q.put((root, 0))

        while not q.empty():
            cur, level = q.get()
            row_map[level] = max(row_map.get(level, cur.val), cur.val)

            if cur.left:
                q.put((cur.left, level + 1))

            if cur.right:
                q.put((cur.right, level + 1))

        return [row_map[i] for i in range(len(row_map))]
