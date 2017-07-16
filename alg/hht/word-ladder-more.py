
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict

        if beginWord == endWord:
            return 1

        self.visit = set()
        self.neighbor = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                self.neighbor[key].append(word)

        queue = [(beginWord, 1)]
        while queue:
            word, steps = queue.pop(0)
            if self.diff(word, endWord) <= 1:
                return steps + 1

            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                for bw in self.neighbor[key]:
                    if bw not in self.visit:
                        self.visit.add(bw)
                        queue.append((bw, steps + 1))

        return 0

    def diff(self, w1, w2):
        d = 0
        for i, j in zip(w1, w2):
            if i != j:
                d += 1
        return d


if __name__ == "__main__":
    print Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
