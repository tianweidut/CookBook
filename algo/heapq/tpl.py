#coding: utf-8
import heapq


def imerge(*iterables):
    h = []
    for it in map(iter, iterables):
        try:
            n = it.next
            # 这里对 it.next obj 进行hash，值没有意义，但是拼成 [n(), hash(n), n] 后能够简单的进行cmp, 避免对it.next 进行排序
            h.append([n(), hash(n), n])
        except StopIteration:
            pass

    heapq.heapify(h)

    while True:
        try:
            while True:
                v, n = s = h[0]
                yield v
                s[0] = n()
                heapq._siftup(h, 0)
        except StopIteration:
            heapq.heappop(h)
        except IndexError:
            return


def heapq_sort(i):
    o = []
    heapq.heapify(o)

    for _i in i:
        heapq.heappush(o, _i)

    return [heapq.heappop(o) for _i in range(len(o))]


if __name__ == "__main__":
    i = imerge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25])
    print list(i)

    print heapq_sort([1,2, 100, 10, 1, 5, 3, 10, 15])
