
class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        if not nums or len(nums) <= 1:
            return nums

        from math import ceil
        sorted_num = sorted(nums)
        mid = int(ceil(len(nums) / 2.0))

        print sorted_num
        print mid
        print len(nums)

        for i, v in enumerate(reversed(sorted_num[0:mid])):
            print i, v
            nums[i * 2] = v

        for i, v in enumerate(reversed(sorted_num[mid:])):
            print i, v
            nums[i * 2 + 1] = v

        return nums


if __name__ == "__main__":
    print Solution().wiggleSort([4, 5, 5, 6])
    print Solution().wiggleSort([1,5,1,1,6,4])
    print Solution().wiggleSort([1,2,1,2,1,1,2,2,1])
