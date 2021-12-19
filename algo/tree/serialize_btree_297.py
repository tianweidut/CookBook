#coding: utf-8

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        print root
        stack = [root]
        serialize_str = ''
        while len(stack) != 0:
            cur = stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                serialize_str += '%s,' % cur.val
            else:
                serialize_str += '#,'

        return serialize_str.strip(',')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = [None if d == '#' else TreeNode(d) for d in data.split(',')]

        root = nodes[0]
        stack = [(root, 'right'), (root, 'left')]
        for node in nodes[1:]:
            cur, attr = stack.pop()
            if node:
                setattr(cur, attr, node)
                stack.append((node, 'right'))
                stack.append((node, 'left'))

        return root


def create_btree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    return root


def create_btree2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)

    return root


def create_btree3():
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(6)

    return root


def create_btree4():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    return root

if __name__ == "__main__":
    #for root in (create_btree(), create_btree2(), create_btree3(), create_btree4()):
    for root in (create_btree4(), ):
        codec = Codec()
        print codec.serialize(root)
        new_root = codec.deserialize(codec.serialize(root))
        print new_root.val, new_root.left.val, new_root.right.val, new_root.right, new_root.left.left
