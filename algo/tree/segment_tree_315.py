# coding: utf-8
# ref: https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class SegmentTreeNode(object):

    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None


class SegmentTree(object):

    def __init__(self):
        self.root = None

    def build(self, root=None, start=0, end=0):
        if root is None:
            root = SegmentTreeNode(start, end, 0)

        if start >= end:
            return root

        mid = (end + start) / 2
        root.left = self.build(start=start, end=mid)
        root.right = self.build(start=mid + 1, end=end)
        return root

    def update(self, root, index, value):
        if root.start == root.end == index:
            root.value += value
            return

        mid = (root.end + root.start) / 2
        root.value += value
        if index <= mid:
            self.update(root.left, index, value)
        else:
            self.update(root.right, index, value)

    def query_sum(self, start, end, root):
        if end < root.start or start > root.end:
            return 0

        if start <= root.start <= root.end <= end:
            return root.value

        left_sum = self.query_sum(start, end, root.left)
        right_sum = self.query_sum(start, end, root.right)
        return left_sum + right_sum


class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        result = []
        reversed_map = {key: i for i, key in enumerate(sorted(set(nums)))}
        root = SegmentTreeNode(start=0, end=len(reversed_map) - 1, value=0)
        st = SegmentTree()
        st.build(root, 0, len(reversed_map) - 1)

        for num in reversed(nums):
            index = reversed_map[num]
            result.append(st.query_sum(0, index - 1, root))

            st.update(root, index, value=1)

        return list(reversed(result))


def main():
    test_suits = (
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([5, 2, 1, 6], [2, 1, 0, 0]),
        ([5], [0]),
        ([5], [0]),
        ([26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41],
         [10, 27, 10, 35, 12, 22, 28, 8, 19, 2, 12, 2, 9, 6, 12, 5, 17, 9, 19, 12, 14, 6, 12, 5, 12, 3, 0, 10, 0, 7, 8, 4, 0, 0, 4, 3, 2, 0, 1, 0]),
    )

    for nums, expected_result in test_suits:
        result = Solution().countSmaller(nums)
        print '----'
        print 'e:', expected_result
        print "r:", result
        print result == expected_result


if __name__ == "__main__":
    main()
