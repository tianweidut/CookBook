#coding: utf-8
# ref: https://leetcode.com/problems/distinct-subsequences/

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t:
            return 0

        return self.run_dsub(s, t)

    def run_lcs(self, s, t):
        self.lcs_arr = [[None for j in t] for i in s]  # s为行，t为列
        return self.lcs(s, len(s) - 1, t, len(t) - 1)

    def lcs(self, s, n, t, m):
        if n < 0 or m < 0:
            return 0

        if self.lcs_arr[n][m] is not None:
            return self.lcs_arr[n][m]

        if s[n] == t[m]:
            cnt = self.lcs(s, n - 1, t, m - 1) + 1
        else:
            cnt = max(self.lcs(s, n - 1, t, m),
                      self.lcs(s, n, t, m - 1))

        self.lcs_arr[n][m] = cnt
        return cnt

    def run_dsub(self, s, t):
        self.dsub_arr = [[None for j in t] for i in s]  # s为行，t为列
        for i in range(len(s)):
            self.dsub_arr[i][0] = 1

        for i in range(1, len(t)):
            self.dsub_arr[0][i] = 0

        return self.dsub(s, len(s) - 1, t, len(t) - 1)

    def dsub(self, s, n, t, m):
        if n < 0 or m < 0:
            return 0

        if self.dsub_arr[n][m] is not None:
            return self.dsub_arr[n][m]

        if s[n] == t[m]:
            return self.dsub(s, n - 1, t, m) + self.dsub(s, n - 1, t, m - 1)
        else:
            return self.dsub(s, n - 1, t, m)


def main():
    s = "rabbbit"
    t = "rabbit"
    num = Solution().numDistinct(s, t)
    print num


if __name__ == "__main__":
    mai()
