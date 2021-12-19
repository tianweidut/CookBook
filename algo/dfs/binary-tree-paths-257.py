# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        all_paths = []
        cur_path = ""
        self.find_path(root, cur_path, all_paths)
        return all_paths

    def find_path(self, root, cur_path, all_paths):
        if root is None:
            return
        elif root.left is None and root.right is None:
            cur_path += str(root.val)
            all_paths.append(cur_path)
        else:
            cur_path += "->%s" % root.val
            self.find_path(root.left, cur_path, all_paths)
            self.find_path(root.right, cur_path, all_paths)


if __name__ == "__main__":
    pass
