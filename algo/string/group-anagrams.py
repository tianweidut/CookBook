class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        r = defaultdict(list)
        for s in strs:
            key = self._k(s)
            r[key].append(s)

        return r.values()

    def _k(self, s):
        cmap = [0] * 26
        for c in s:
            cmap[ord(c) - ord('a')] += 1

        return "".join(map(str, cmap))
