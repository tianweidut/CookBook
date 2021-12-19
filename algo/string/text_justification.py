#coding: utf-8


class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words or maxWidth <= 0:
            return [""]

        rs = []
        per_line_words = []
        line_len = 0
        for word in words:
            line_len += len(word)

            if line_len > maxWidth:
                blanks = self.calculate_blanks(per_line_words, maxWidth)
                line_str = self.generate_line_str(per_line_words, blanks)
                rs.append(line_str)

                per_line_words = []
                per_line_words.append(word)
                line_len = len(word) + 1
            else:
                per_line_words.append(word)
                line_len += 1

        #last line left-justification
        if per_line_words:
            rs.append(' '.join(per_line_words))

        output = []
        for line in rs:
            blanks = max(maxWidth - len(line), 0)
            output.append(line + blanks * ' ')

        return output

    def calculate_blanks(self, per_line_words, maxWidth):
        word_cnt = len(per_line_words)
        word_len = sum([len(w) for w in per_line_words])

        left = maxWidth - word_len
        num = word_cnt - 1
        
        if num <= 0:
            return [0]

        per = left / num 

        rs = [per] * num 

        for i in range(0, left % num):
            rs[i] += 1

        return rs + [0]

    def generate_line_str(self, per_line_words, blanks):
        rs = ''
        for i, j in zip(per_line_words, blanks):
            rs += i + ' ' * j
        return rs


def main():
    dataset = [
        [6,  ["Listen","to","many,","speak","to","a","few."]],
        [17, ["This", "is", "an", "example", "of", "text", "justification."]],
        [100, ["This", "is", "an", "example", "of", "text", "justification."]],
        [2, [""]],
    ]

    for n, w in dataset:
        print Solution().fullJustify(w, n)


if __name__ == "__main__":
    main()
