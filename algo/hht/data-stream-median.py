

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        if not nums:
            return []

        import heapq
        max_heap = [-nums[0]]
        min_heap = []
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        r = [nums[0]]
        for num in nums[1:]:
            len_max_heap = len(max_heap)
            len_min_heap = len(min_heap)

            if 0 < len_max_heap - len_min_heap <= 1:
                max_top = - max_heap[0]
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
            r.append(-max_heap[0])
        return r


if __name__ == "__main__":
    print Solution().medianII([1, 2, 3, 4, 5])
    print Solution().medianII([4, 5, 1, 3, 2, 6, 0])
    print Solution().medianII([2, 20, 100])
