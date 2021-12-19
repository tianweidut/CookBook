
class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.boards = {'1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",
                       '7': "pqrs", '8': "tuv", '9': "wxyz", '0': ""}

        self.r = []
        self.digits = digits
        self.len_d = len(digits)
        self.dfs(0, "")

        return self.r

    def dfs(self, pos, s):
        if pos == self.len_d:
            if s:
                self.r.append(s)
            return

        for c in self.boards[self.digits[pos]]:
            self.dfs(pos + 1, s + c)
