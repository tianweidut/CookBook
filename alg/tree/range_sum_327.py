#coding: utf-8

class SegmentTreeNode(object):

    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None


class FenwickTree(object):

    def __init__(self, n):
        self.nums = [0] * (n + 1)
        self.n = n

    def lowbit(self, x):
        return x & (-x)

    def add(self, index, value):
        while index <= self.n:
            self.nums[index] += value
            index += self.lowbit(index)

    def sum(self, index):
        r = 0
        while index > 0:
            r += self.nums[index]
            index -= self.lowbit(index)
        return r


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
    def countRangeSumTLE(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        root = SegmentTreeNode(start=0, end=len(nums) - 1, value=0)
        st = SegmentTree()
        st.build(root, 0, len(nums) - 1)

        for i, n in enumerate(nums):
            st.update(root, i, n)

        cnt = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                r = st.query_sum(i, j, root)
                if lower <= r <= upper:
                    cnt += 1

        return cnt

    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0

        total = 0
        sum_array = [lower - 1, upper]

        for n in nums:
            total += n
            sum_array += [total, lower - 1 + total, upper + total]

        index = {}
        for i, v in enumerate(sorted(set(sum_array))):
            index[v] = i + 1

        ans = 0
        tree = FenwickTree(len(index))
        for num in reversed(nums):
            tree.add(index[total], 1)
            total -= num
            ans += tree.sum(index[upper + total]) - tree.sum(index[lower - 1 + total])

        return ans


if __name__ == "__main__":
    r = Solution().countRangeSum([-2, 5, -1], -2, 2)
    print r
