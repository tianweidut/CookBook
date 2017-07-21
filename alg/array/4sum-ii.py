class Solution(object):

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d_map_first = defaultdict(int)
        d_map_second = defaultdict(int)
        len_n = len(A)

        self.combine(A, B, len_n, d_map_first)
        self.combine(C, D, len_n, d_map_second)

        r = 0
        for k1, v1 in d_map_first.items():
            remain = -k1
            if remain in d_map_second:
                r += v1 * d_map_second[remain]

        return r

    def combine(self, M, N, len_n, d_map):
        for i in range(len_n):
            for j in range(len_n):
                d_map[M[i] + N[j]] += 1
