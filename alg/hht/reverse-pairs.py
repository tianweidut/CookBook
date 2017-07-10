
class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs

    def reversePairs(self, A):
        if not A or len(A) <= 1:
            return 0

        cnt = self.merge_sort(A, 0, len(A) - 1)
        return cnt

    def merge_sort(self, A, start, end):
        if start >= end:
            return 0

        mid = start + (end - start) / 2
        left = self.merge_sort(A, start, mid)
        right = self.merge_sort(A, mid + 1, end)

        cnt = 0
        prev = mid
        next = end

        B = [0] * (end - start + 1)
        i = end - start

        while prev >= start and next >= mid + 1:
            if A[prev] <= A[next]:
                B[i] = A[next]
                next -= 1
            else:
                B[i] = A[prev]
                prev -= 1
                cnt += (next - mid)
            i -= 1

        while prev >= start:
            B[i] = A[prev]
            i -= 1
            prev -= 1

        while next >= mid + 1:
            B[i] = A[next]
            next -= 1
            i -= 1

        A[start:end + 1] = B

        return left + right + cnt
