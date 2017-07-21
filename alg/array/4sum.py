class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        len_n = len(nums)
        if len_n < 4:
            return []

        nums = sorted(nums)
        r = []

        for fixed in range(len_n - 3):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            if nums[fixed] + nums[fixed + 1] + nums[fixed + 2] + nums[fixed + 3] > target:
                break

            if nums[fixed] + nums[len_n - 1] + nums[len_n - 2] + nums[len_n - 3] < target:
                continue

            for s_fixed in range(fixed + 1, len_n - 2):
                if s_fixed > fixed + 1 and nums[s_fixed] == nums[s_fixed - 1]:
                    continue

                if nums[fixed] + nums[s_fixed] + nums[s_fixed + 1] + nums[s_fixed + 2] > target:
                    break

                if nums[fixed] + nums[s_fixed] + nums[len_n - 1] + nums[len_n - 2] < target:
                    continue

                i = s_fixed + 1
                j = len_n - 1

                while i < j:
                    delta = target - nums[fixed] - \
                        nums[s_fixed] - nums[i] - nums[j]

                    if delta > 0:
                        i += 1
                    elif delta < 0:
                        j -= 1
                    else:
                        r.append(
                            [nums[fixed], nums[s_fixed], nums[i], nums[j]])

                        j -= 1
                        i += 1

                        while i < j and nums[i] == nums[i - 1]:
                            i += 1

                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1

        return r
