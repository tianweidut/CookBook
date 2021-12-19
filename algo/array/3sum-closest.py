
class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)

        if len_nums < 3:
            return None

        nums = sorted(nums)
        import sys
        r = sys.maxsize

        for fixed in range(len_nums - 2):
            i = fixed + 1
            j = len_nums - 1

            while i < j:
                delta = target - nums[fixed] - nums[i] - nums[j]
                if delta == 0:
                    return target

                r = r if abs(r) < abs(delta) else delta
                if delta > 0:
                    i += 1
                else:
                    j -= 1

        return target - r
