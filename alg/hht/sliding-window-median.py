class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or k <= 1:
            return nums

        import heapq
        max_heap = [-nums[0]]
        min_heap = []
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        r = []
        for i, num in enumerate(nums[1:], 1):
            if i > k - 1:
                pop_num = nums[i - k]
                if pop_num > -max_heap[0]:
                    min_heap.remove(pop_num)
                    heapq.heapify(min_heap)
                else:
                    max_heap.remove(-pop_num)
                    heapq.heapify(max_heap)

            len_max_heap = len(max_heap)
            len_min_heap = len(min_heap)

            if 0 <= len_max_heap - len_min_heap <= 1 or not min_heap:
                max_top = max_heap[0]
                max_top = -max_top
                if num >= max_top:
                    heapq.heappush(min_heap, num)
                else:
                    heapq.heappush(min_heap, max_top)
                    heapq.heappushpop(max_heap, -num)
            else:
                min_top = min_heap[0]
                if num > min_top:
                    heapq.heappushpop(min_heap, num)
                    heapq.heappush(max_heap, -min_top)
                else:
                    heapq.heappush(max_heap, -num)

            if i >= k - 1:
                if len(max_heap) >= len(min_heap):
                    r.append(-max_heap[0])
                else:
                    r.append(min_heap[0])
        return r


if __name__ == "__main__":
    #print Solution().medianSlidingWindow([1, 2, 7, 8, 5], k=3)
    #print Solution().medianSlidingWindow([1, 2, 7, 7, 2], k=1)
    print Solution().medianSlidingWindow([1980,534,251,1358,1779,732,787,1074,640,1392,1388,434,779,912,1123,94,1377,1540], k=3)
