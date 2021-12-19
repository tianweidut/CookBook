
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array

    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        while start < end - 1:
            mid = (end - start) / 2 + start

            if nums[start] == nums[mid] == nums[end]:
                return min(nums[start: end + 1])
            elif nums[start] <= nums[mid] <= nums[end]:
                return nums[start]
            elif nums[mid] <= nums[end]:
                end = mid
            elif nums[mid] >= nums[start]:
                start = mid

        return min(nums[end], nums[start])


if __name__ == "__main__":
    print Solution().findMin([1, 1, 1, 1, 1, -1, 1, 1, 1, 1])
    print Solution().findMin([2, 1])
    print Solution().findMin([1, 2, 3])
    print Solution().findMin([0, 1, 2, 3, 4, 5, 6])
    print Solution().findMin([4, 5, 6, 0, 1, 2, 3])
    print Solution().findMin([1, 2, 3, 4, 5, 6, 0])
    print Solution().findMin([4, 4, 5, 6, 7, 0, 1, 2])
