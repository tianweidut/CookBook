
class Solution(object):

    def wordBreak_dp(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        is_matched = [False] * (n + 1)
        is_matched[0] = True

        wordDict = set(wordDict)
        for i in range(1, n + 1):
            for j in range(0, i):
                if is_matched[j] and s[j:i] in wordDict:
                    is_matched[i] = True
                    break

        return is_matched[n]

    def wordBreak(self, s, wordDict):
        self.wordDict = wordDict
        self.cached = {}

        return self.dfs(s)

    def dfs(self, s):
        if not s:
            return True

        n = len(s)
        if n in self.cached:
            return self.cached[n]

        flag = False

        for i in range(n - 1, -1, -1):
            prev = s[0: i]
            word = s[i:]
            r = self.dfs(prev) and word in self.wordDict
            if r:
                flag = True
                break

        self.cached[n] = flag
        return flag
