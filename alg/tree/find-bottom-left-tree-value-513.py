# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        from Queue import Queue

        q = Queue()

        q.put((root, 0))
        level_map = {}

        while not q.empty():
            cur, level = q.get()
            if level not in level_map:
                level_map[level] = cur.val

            if cur.left:
                q.put((cur.left, level + 1))

            if cur.right:
                q.put((cur.right, level + 1))

        return level_map[len(level_map) - 1]
