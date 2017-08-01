# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        cnt = len(intervals)
        while i < cnt:
            if intervals[i].start >= newInterval.start:
                intervals.insert(i, newInterval)
                break
            i += 1

        if i == cnt:
            intervals.append(newInterval)

        r = []

        i = 0
        j = i + 1
        while j < cnt + 1:
            e1 = intervals[i].end
            s2 = intervals[j].start
            print e1, s2
            if e1 >= s2:
                intervals[i].end = max(e1, intervals[j].end)
            else:
                r.append(intervals[i])
                i = j
            j += 1

        r.append(intervals[i])

        return r
