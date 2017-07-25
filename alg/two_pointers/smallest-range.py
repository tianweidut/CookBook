

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []

        cnt_k = len(nums)
        if cnt_k == 1:
            return [nums[0][0], nums[0][0]]

        import sys
        import heapq
        from collections import defaultdict
        sorted_nums = []
        heap = [(n[0], ki, 0) for ki, n in enumerate(nums)]
        heapq.heapify(heap)
        while heap:
            v, ki, i = heapq.heappop(heap)
            sorted_nums.append((v, ki))
            i += 1
            if i < len(nums[ki]):
                heapq.heappush(heap, (nums[ki][i], ki, i))

        i = j = 0
        cnt = 0
        saved_map = defaultdict(int)
        min_start = 0
        min_end = sys.maxint

        while j < len(sorted_nums):
            v, ki = sorted_nums[j]

            saved_map[ki] += 1
            if saved_map[ki] == 1:
                cnt += 1

            while cnt == cnt_k:
                if min_end - min_start > sorted_nums[j][0] - sorted_nums[i][0]:
                    min_end = sorted_nums[j][0]
                    min_start = sorted_nums[i][0]

                _, _ki = sorted_nums[i]
                if saved_map[_ki] == 1:
                    cnt -= 1

                saved_map[_ki] -= 1
                i += 1

            j += 1

        return [min_start, min_end]


if __name__ == "__main__":
    print Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
