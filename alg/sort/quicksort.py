# coding: utf-8


def quicksort(nums, start=None, end=None):
    start = 0 if start is None else start
    end = len(nums) - 1 if end is None else end

    if start >= end:
        return

    pivot = partition(nums, start, end)
    quicksort(nums, start, pivot - 1)
    quicksort(nums, pivot + 1, end)


def quicksort_iter(nums, start=None, end=None):
    start = 0 if start is None else start
    end = len(nums) - 1 if end is None else end

    if start >= end:
        return

    queue = [(start, end)]

    while queue:
        s, e = queue.pop(0)
        if s >= e:
            continue

        pivot = partition(nums, s, e)
        queue.append((s, pivot - 1))
        queue.append((pivot + 1, e))


def partition(nums, start, end):
    pval = nums[start]

    while start < end:
        while start < end and nums[end] >= pval:
            end -= 1

        if start < end:
            nums[start] = nums[end]
            start += 1

        while start < end and nums[start] < pval:
            start += 1

        if start < end:
            nums[end] = nums[start]
            end -= 1

    nums[start] = pval
    return start


if __name__ == "__main__":
    r = [1, 4, 5, 10, 11, 23, 4, 3, 7, 9, 8]
    #quicksort(r)
    quicksort_iter(r)
    print r
