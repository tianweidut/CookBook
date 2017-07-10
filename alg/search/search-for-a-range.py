
class Solution:

    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        return self.bsearch(A, 0, len(A) - 1, target)

    def bsearch(self, A, s, e, target):
        if not A or target < A[0]:
            return [-1, -1]

        while s <= e:
            mid = s + (e - s) / 2

            if A[mid] == target:
                ls, le = self.bsearch(A, s, mid - 1, target)
                rs, re = self.bsearch(A, mid + 1, e, target)
                return [mid if ls == -1 else ls, mid if re == -1 else re]
            elif A[mid] > target:
                e = mid - 1
            else:
                s = mid + 1

        return [-1, -1]
