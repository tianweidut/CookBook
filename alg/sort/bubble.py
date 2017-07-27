#coding: utf-8

#通过交换使相邻的两个数变成小数在前大数在后，
#这样每次遍历后，最大的数就“沉”到最后面了。重复N次即可以使数组有序。
def bubble_sort(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(1, n - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


#每次将一个待排序的数据，插入到前面已经排好序的序列之中，直到全部数据插入完成。
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


#数组分成有序区和无序区，初始时整个数组都是无序区
#然后每次从无序区选一个最小的元素直接放到有序区的最后，直到整个数组变有序区。
def select_sort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        for j in range(i, n):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]


if __name__ == "__main__":
    data = [3, 4, 5, 1, 6, 7, 9, 8, 2]
    bubble_sort(data)
    print data

    data = [3, 4, 5, 1, 6, 7, 9, 8, 2, 0, 0]
    select_sort(data)
    print data

    data = [3, 4, 5, 1, 6, 7, 9, 8, 2, 0, 0]
    insert_sort(data)
    print data
