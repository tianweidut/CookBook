
class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        from collections import defaultdict
        keys = defaultdict(int)
        for c in s:
            keys[c] += 1

        max_cnt = 0
        vals = defaultdict(list)
        for k, v in keys.iteritems():
            max_cnt = max(max_cnt, v)
            vals[v].append(k)

        r = ""
        for i in range(max_cnt, -1, -1):
            if i in vals:
                r += "".join([c * i for c in vals[i]])
        return r
