
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 4:
            return False

        total = sum(nums)
        if total % 4 != 0:
            return False

        target = total / 4
        nums = sorted(nums, reverse=True)
        cuc_sums = [0] * 4
        return self.dfs(nums, target, 0, cuc_sums)

    def dfs(self, nums, target, index, cuc_sums):
        if index >= len(nums):
            return all([cuc_sums[i] == target for i in range(3)])

        if nums[index] > target:
            return False

        for i in range(4):
            if cuc_sums[i] + nums[index] > target:
                continue

            cuc_sums[i] += nums[index]
            if self.dfs(nums, target, index + 1, cuc_sums):
                return True
            cuc_sums[i] -= nums[index]

        return False


def main():
    print Solution().makesquare([1, 1, 2, 2, 2])
    print Solution().makesquare([3, 3, 3, 3, 4])

if __name__ == "__main__":
    main()
