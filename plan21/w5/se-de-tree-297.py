# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        queue = deque()
        queue.append(root)
        
        s = []
        while queue:
            n = queue.popleft()
            if n:
                s.append(str(n.val))
                queue.append(n.left)
                queue.append(n.right)
            else:
                s.append("#")
        return ",".join(s)

    def deserialize(self, s):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not s:
            return None
        
        s = s.split(",")
        root = TreeNode(int(s[0]))
        queue = deque()
        queue.append(root)
        
        idx = 1
        while queue:
            n = queue.popleft()
            if s[idx] == "#":
                n.left = None
            else:
                n.left = TreeNode(int(s[idx]))
                queue.append(n.left)
            
            if s[idx+1] == "#":
                n.right = None
            else:
                n.right = TreeNode(int(s[idx+1]))
                queue.append(n.right)
                
            idx += 2
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))