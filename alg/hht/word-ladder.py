
import copy
import sys

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = copy.copy(wordList)
        init = sys.maxsize
        self.min_steps = init
        self.do_ladder(beginWord, endWord, wordList, 1)
        return self.min_steps if self.min_steps != init else 0

    def do_ladder(self, bw, ew, word_list, steps):
        if not word_list:
            return

        if self.diff(bw, ew) == 1:
            self.min_steps = min(self.min_steps, steps + 1)
            return

        transformed_words = [w for w in word_list if self.diff(bw, w) == 1]
        for w in transformed_words:
            if self.diff(w, ew) == 1:
                self.min_steps = min(self.min_steps, steps + 2)
            else:
                new_wl = copy.copy(word_list)
                new_wl.remove(w)
                self.do_ladder(w, ew, new_wl, steps + 1)

    def diff(self, w1, w2):
        d = 0
        for i, j in zip(w1, w2):
            if i != j:
                d += 1
        return d

if __name__ == "__main__":
    print Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
