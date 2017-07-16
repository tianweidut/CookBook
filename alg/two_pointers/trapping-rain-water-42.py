

class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_h = len(height)

        if not height or len_h < 3:
            return 0

        water = 0
        i = 0
        j = len(height) - 1

        lmax = height[i]
        rmax = height[j]

        while i < j:
            if lmax < rmax:
                i += 1
                if height[i] >= lmax:
                    lmax = height[i]
                else:
                    water += lmax - height[i]
            else:
                j -= 1
                if height[j] >= rmax:
                    rmax = height[j]
                else:
                    water += rmax - height[j]

        return water

if __name__ == "__main__":
    print Solution().trap([4, 2, 3])
    # print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    # print Solution().trap([0, 2, 0])
