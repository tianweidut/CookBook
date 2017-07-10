

def search(nums, target):
    if not nums:
        return -1

    s = 0
    e = len(nums) - 1

    while s <= e:
        mid = s + (e - s) / 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            s = mid + 1
        else:
            e = mid - 1

    return -1


if __name__ == "__main__":
    print search([1,2,3,4,5,6,7,8], 10)
    print search([1,2,3,4,5,6,7,8], 5)
    print search([1,2,3,4,5,6,7,8], 1)
    print search([1,2,3,4,5,6,7,8], 3)
    print search([1,2,3,4,5,6,7,8], 4)
    print search([1,2,3,4,5,6,7,8], 5.5)
