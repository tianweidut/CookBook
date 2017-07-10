

class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''

    def serialize(self, root):
        if not root:
            return ""

        r = []
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root:
                r.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                r.append("#")

        return ",".join(map(str, r))

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''

    def deserialize(self, data):
        data = data.strip().lstrip('#')
        if not data:
            return None

        vals = data.split(',')

        phead = root = TreeNode(vals[0])
        root_queue = [root]

        i = 1
        while i < len(vals):
            root = root_queue.pop(0)
            left_v = vals[i]
            right_v = vals[i + 1]

            if left_v == "#":
                root.left = None
            else:
                root.left = TreeNode(left_v)
                root_queue.append(root.left)

            if right_v == "#":
                root.right = None
            else:
                root.right = TreeNode(right_v)
                root_queue.append(root.right)
            i += 2

        return phead
