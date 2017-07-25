
class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 or not s2:
            return False

        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s2 < len_s1:
            return False

        s1_map = [0] * 26
        for c in s1:
            s1_map[ord(c) - ord('a')] += 1

        window_map = [0] * 26

        i = j = 0
        while j < len_s2:
            window_map[ord(s2[j]) - ord('a')] += 1

            if j - i + 1 == len_s1:
                if window_map == s1_map:
                    return True
                else:
                    window_map[ord(s2[i]) - ord('a')] -= 1
                    i += 1
            j += 1

        return False
