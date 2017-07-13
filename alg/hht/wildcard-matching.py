
class Solution:

    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        self.record = {}
        return self.do_match(list(s), 0, list(p), 0)

    def do_match(self, s, s_start, p, p_start):
        key = (s_start, p_start)
        if key in self.record:
            return self.record[key]

        len_s = len(s)
        len_p = len(p)

        flag = None
        while s_start < len_s and p_start < len_p:
            if p[p_start] == s[s_start] or p[p_start] == '?':
                p_start += 1
                s_start += 1
            else:
                if p[p_start] == '*':
                    flag = (self.do_match(s, s_start + 1, p, p_start) or
                            self.do_match(s, s_start + 1, p, p_start + 1) or
                            self.do_match(s, s_start, p, p_start + 1))
                else:
                    flag = False
                break

        if flag is not None:
            flag = flag
        elif s_start == len_s and p_start == len_p:
            flag = True
        elif p_start == len_p and s_start < len_s:
            flag = False
        elif s_start == len_s and p_start < len_p:
            flag = all([pp == '*' for pp in p[p_start:]])

        self.record[key] = flag
        return flag
