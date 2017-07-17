
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.max_len = 1
        self.max_start_pos = 0

        for i in range(0, len(s) - 1):
            self._chk_palindromiac(s, i, i)
            self._chk_palindromiac(s, i, i + 1)

        return s[self.max_start_pos:self.max_len + self.max_start_pos]

    def _chk_palindromiac(self, s, i, j):
        while i >= 0 and j <= len(s) - 1:
            if s[i] != s[j]:
                break
            i -= 1
            j += 1

            p_len = j - i - 1
            if p_len > self.max_len:
                self.max_len = p_len
                self.max_start_pos = i + 1
