#coding: utf-8


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not s or not d:
            return ''

        sorted_d = sorted(d,
                          cmp=lambda x, y: cmp(len(x), len(y)) if len(x) != len(y) else cmp(y, x),
                          reverse=True)
        print sorted_d

        for di in sorted_d:
            if self.chk_sub(s, di):
                return di

        return ''

    def chk_sub(self, s, di):
        i = 0
        j = 0

        while True:
            if i == len(di) or j == len(s):
                return False

            if di[i] == s[j]:
                i += 1
                j += 1
                if i == len(di):
                    return True
            else:
                j += 1


def main():
    r = Solution().findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"])
    print r

    r = Solution().findLongestWord("abpcplea", ["a", "b", "c"])
    print r


if __name__ == "__main__":
    main()
