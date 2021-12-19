#coding: utf-8


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ''

        def _join(s):
            return ''.join(map(str, s))

        s_nums = sorted(nums,
                        cmp=lambda a, b: cmp(_join([a, b]), _join([b, a])),
                        reverse=True)
        r = _join(s_nums)
        if r.startswith('0'):
            r = '0'

        return r


def main():
    lastest_num_str = Solution().largestNumber([3, 30, 34, 5, 9])
    print lastest_num_str


if __name__ == "__main__":
    main()
