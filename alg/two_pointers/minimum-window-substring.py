class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s or len(t) > len(s):
            return ""

        from collections import defaultdict
        map_t = defaultdict(int)
        for c in t:
            map_t[c] += 1

        len_t = len(t)
        len_s = len(s)

        i = j = 0
        cnt = 0
        min_len = len_s + 1
        min_start = 0

        while j < len_s:
            if s[j] in map_t:
                map_t[s[j]] -= 1

                if map_t[s[j]] >= 0:
                    cnt += 1

            while cnt == len_t:
                if min_len > j - i + 1:
                    min_len = j - i + 1
                    min_start = i

                if s[i] in map_t:
                    if map_t[s[i]] >= 0:
                        cnt -= 1
                    map_t[s[i]] += 1
                i += 1
            j += 1

        if min_len == len_s + 1:
            return ""

        return s[min_start: min_start + min_len]
