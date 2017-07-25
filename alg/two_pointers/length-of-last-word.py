
class Solution(object):

    def lengthOfLastWord_with_split(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        return len(s.split()[-1])

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        len_s = len(s)
        i = j = 0
        last_word = 0

        while j < len_s:
            if s[j] == ' ':
                last_word = j - i

                while j < len_s and s[j] == ' ':
                    j += 1

                i = j
            else:
                j += 1

        if i != j:
            last_word = j - i

        return last_word
