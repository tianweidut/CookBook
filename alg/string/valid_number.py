#coding: utf-8

class Solution(object):
        def isNumber(self, s):
            s = s.strip()

            if not s:
                return False

            if s[0] not in ('+', '-') and not self.is_num(s[0]):
                return False

            for e in s[1:]:
                if not self.is_num(e):
                    return False
            return True 

        def is_num(self, e):
            try:
                int(e)
            except:
                return False
            else:
                return True



if __name__ == "__main__":
    dataset = [
        ["0", True],
        [" 0.1 ", True],
        ["abc", False],
        ["1 a", False],
        ["2e10", True],
        ["", False],
        ["-25", True],
        ["+25", True],
        ["25-", True],
    ]

    for s, v in dataset:
        assert(v == Solution().isNumber(s))
