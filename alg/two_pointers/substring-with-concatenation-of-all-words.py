
class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        size_n = len(words)
        size_w = len(words[0])

        if size_n > len(s):
            return []

        import copy
        from collections import defaultdict
        map_w = defaultdict(int)
        for w in words:
            map_w[w] += 1

        r = []
        i = j = 0
        distance = size_n * size_w
        j = i + distance - 1

        while j < len(s):

            cnt = 0
            copy_map_w = copy.copy(map_w)
            for wi in range(i, j + 1, size_w):
                w = s[wi:wi + size_w]
                if w in copy_map_w and copy_map_w[w] > 0:
                    copy_map_w[w] -= 1
                    cnt += 1
                else:
                    break

                if cnt == size_n:
                    r.append(i)

            i += 1
            j = i + distance - 1

        return r
