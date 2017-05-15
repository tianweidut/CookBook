
class UnionFind(object):
    def __init__(self, n):
        self.nums = [i for i in range(n)]
        self.sz = [1] * n
        self.n = n
        self.count = n

    def find(self, i):
        while i != self.nums[i]:
            self.nums[i] = self.nums[self.nums[i]]
            i = self.nums[i]

        return i

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)

        if ri == rj:
            return

        if self.sz[ri] <= self.sz[rj]:
            self.nums[ri] = rj
            self.sz[rj] += self.sz[ri]
        else:
            self.nums[rj] = ri
            self.sz[ri] += self.sz[rj]

        self.count -= 1

    def cal_set(self):
        r = set()
        for i in range(self.n):
            ri = self.find(i)
            r.add(ri)
        return len(r)


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        cnt = len(M)
        uf = UnionFind(cnt)

        for i in range(cnt - 1):
            for j in range(i + 1, cnt):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.cal_set()

def main():
    #print Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    #print Solution().findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]])

    m = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
         [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
         [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
         [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
         [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
         [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
         [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
    print Solution().findCircleNum(m)
    m = [[1,1,1],[1,1,1],[1,1,1]]
    print Solution().findCircleNum(m)

if __name__ == "__main__":
    main()
