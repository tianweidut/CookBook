

class Solution:
    def maxSlidingWindow_with_max_heap(self, nums, k):
        if not nums:
            return nums

        if k < 0 or len(nums) < k:
            return max(nums)

        import heapq
        max_heap = [(-n, i) for i, n in enumerate(nums[:k - 1])]
        heapq.heapify(max_heap)

        r = []
        for i in range(k - 1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            r.append(-max_heap[0][0])
        return r

    def maxSlidingWindow(self, nums, k):
        if not nums or k < 0:
            return nums

        queue = []
        r = []
        for i, n in enumerate(nums):
            if not queue or n <= queue[-1][1]:
                queue.append((i, n))
            else:
                while queue and queue[-1][1] < n:
                    queue.pop()
                queue.append((i, n))

            top_i, top_n = queue[0]
            if i - top_i >= k:
                queue.pop(0)

            if i >= k - 1:
                r.append(queue[0][1])
        return r


if __name__ == "__main__":
    print Solution().maxSlidingWindow([1, 2, 7, 7, 8], 3)
