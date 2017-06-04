#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        from Queue import Queue
        q = Queue()

        q.put((root, 0))
        cur_level = 0

        r = []

        while not q.empty():
            cur, level = q.get()
            if level != cur_level:
                r.append(cur.val)

            if cur.left:
                q.put((cur.left, level + 1))
            if cur.right:
                q.put((cur.right, level + 1))

        return r

if __name__ == "__main__":
    pass
