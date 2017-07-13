

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        self.record = {}
        return self.do_match(list(s), 0, list(p), 0)

    def do_match(self, s, si, p, pi):
        key = (si, pi)
        if key in self.record:
            return self.record[key]

        if pi >= len(p):
            flag = si >= len(s)
        elif pi + 1 < len(p) and p[pi + 1] == '*':
            flag1 = self.do_match(s, si, p, pi + 2)
            flag2 = si < len(s) and (s[si] == p[pi] or p[pi] == '.') and self.do_match(s, si + 1, p, pi)
            flag = flag1 or flag2
        else:
            flag = si < len(s) and (s[si] == p[pi] or p[pi] == '.') and self.do_match(s, si + 1, p, pi + 1)

        self.record[key] = flag
        return flag
