
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_h = 0

        while left < right:
            left_v = height[left]
            right_v = height[right]
            max_h = max(max_h, (right - left) * min(left_v, right_v))
            if left_v < right_v:
                left += 1
            else:
                right -= 1

        return max_h
