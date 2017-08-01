
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: x.start)
        r = []

        i = 0
        j = 1
        while j < len(intervals):
            e1 = intervals[i].end
            s2 = intervals[j].start

            if e1 >= s2:
                intervals[i].end = max(e1, intervals[j].end)
            else:
                r.append([intervals[i].start, intervals[i].end])
                i = j
            j += 1

        r.append([intervals[i].start, intervals[i].end])
        return r
