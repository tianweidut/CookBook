def ms(nums, start, end):
    if start >= end:
        return

    m = start + (end - start) / 2
    ms(nums, start, m)
    ms(nums, m + 1, end)
    mg(nums, start, m, m + 1, end)


def mg(nums, s1, e1, s2, e2):
    n1 = nums[s1:e1 + 1]
    n2 = nums[s2:e2 + 1]

    k = s1
    i = 0
    j = 0
    while i <= e1 - s1 and j <= e2 - s2:
        if n1[i] < n2[j]:
            nums[k] = n1[i]
            i += 1
        else:
            nums[k] = n2[j]
            j += 1

        k += 1

    while i <= e1 - s1:
        nums[k] = n1[i]
        k += 1
        i += 1

    while j <= e2 - s2:
        nums[k] = n2[j]
        k += 1
        j += 1


if __name__ == "__main__":
    a = [1,4,5,2,3]
    ms(a, 0, len(a) - 1)
    print a
