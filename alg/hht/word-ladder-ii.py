class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def findLadders(self, start, end, dict):
        from collections import defaultdict

        if start == end:
            return [[start, end]]

        dict.add(start)
        dict.add(end)
        neighbors = defaultdict(set)
        len_word = len(start)

        for word in dict:
            for i in range(len_word):
                for j in range(ord('a'), ord('z') + 1):
                    key = word[:i] + chr(j) + word[i + 1:]
                    if key in dict:
                        neighbors[word].add(key)
                        neighbors[key].add(word)

        queue = [(start, [start])]
        transformed_list = []
        flag = False
        visited = set([start])

        while not flag and queue:
            lwords = []

            for i in range(len(queue)):
                word, wlist = queue.pop(0)

                if word == end:
                    transformed_list.append(wlist)
                    flag = True

                for nword in neighbors[word]:
                    if nword not in visited:
                        queue.append((nword, wlist + [nword]))
                        lwords.append(nword)

            visited.update(lwords)

        return transformed_list

if __name__ == "__main__":
    print Solution().findLadders("qa", "sq", [])
