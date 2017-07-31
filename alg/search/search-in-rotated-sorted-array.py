
class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end - start) / 2 + start

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                if nums[mid] >= nums[start]:
                    if target >= nums[start]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] <= nums[end]:
                    if target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    start = mid + 1

        return -1
