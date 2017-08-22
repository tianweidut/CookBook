# http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.htm
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        stack = [0]
        max_area = 0
        
        pos = 1
        heights.append(0)
        
        while pos < len(heights):
            if not stack or heights[stack[-1]] <= heights[pos]:
                stack.append(pos)
                pos += 1
            else:
                top_pos = stack.pop()
                max_area = max(max_area, heights[top_pos] * (pos - stack[-1] - 1 if stack else pos))
                
        return max_area
