#coding: utf-8
import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True 

        serialized_list = self.serialized_tree(root)
        print serialized_list
        len_list = len(serialized_list)

        start = 0
        for factor in range(int(math.log(len_list)) + 3):
            target_nums = int(math.pow(2, factor))
            end = start + target_nums
            end = min(end, len_list)
            print start, end, serialized_list[start:end], self.check_symmetric(serialized_list[start:end])

            if start >= len_list:
                return True

            if not self.check_symmetric(serialized_list[start:end]):
                return False

            start = end

    def check_symmetric(self, val_list):
        num = len(val_list)

        if num == 1:
            return True

        for i in range(num / 2):
            if val_list[i] == '#':
                continue

            if val_list[i] != val_list[-(i + 1)]:
                return False

        return True

    def serialized_tree(self, root):
        import Queue
        queue = Queue.Queue()

        queue.put(root)
        serialized_list = [root.val]

        while not queue.empty():
            cur = queue.get()

            if cur.left:
                queue.put(cur.left)
                append_value = cur.left.val
            else:
                append_value = '#'

            serialized_list.append(append_value)

            if cur.right:
                queue.put(cur.right)
                append_value = cur.right.val
            else:
                append_value = '#'

            serialized_list.append(append_value)

        for i in range(len(serialized_list)):
            if serialized_list[-(i + 1)] != '#':
                serialized_list = serialized_list[0: (-i)]
                break

        return serialized_list


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

if __name__ == "__main__":
    root = create_btree()
    print Solution().serialized_tree(root)
    print Solution().isSymmetric(root)

    root = create_btree2()
    print Solution().serialized_tree(root)
    print Solution().isSymmetric(root)

    root = create_btree3()
    print Solution().serialized_tree(root)
    print Solution().isSymmetric(root)
