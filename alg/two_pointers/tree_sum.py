
class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)
        len_nums = len(nums)
        r = []

        for fixed in range(len_nums):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            i = fixed + 1
            j = len_nums - 1
            while i < j:
                target = nums[fixed] + nums[i] + nums[j]
                if target > 0:
                    j -= 1
                elif target < 0:
                    i += 1
                else:
                    r.append([nums[fixed], nums[i], nums[j]])

                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return r
