
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        self.r = []
        self.n = n
        self.dfs(1, "(", 1, 0)

        return self.r

    def dfs(self, pos, path, left, right):
        if pos == 2 * self.n:
            if right == left == self.n:
                self.r.append(path)
            return

        if left == right:
            self.dfs(pos + 1, path + "(", left + 1, right)
        elif right < left:
            self.dfs(pos + 1, path + ")", left, right + 1)
            if left < self.n:
                self.dfs(pos + 1, path + "(", left + 1, right)
