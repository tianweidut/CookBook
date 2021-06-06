#conding: utf-8

def _bs(data, target, start, end):
    if start > end:
        return False, -1

    mid = (start + end) // 2

    if data[mid] == target:
        return True, mid
    elif target > data[mid]:
        return _bs(data, target, mid + 1, end)
    else:
        return _bs(data, target, start, mid - 1)

def bs(data, target):
    if not data:
        return False, -1

    return _bs(data, target, 0, len(data)-1)

if __name__ == "__main__":
    input = [1,2,3,4,5,6,7,8]
    print(bs(input, 10))
    print(bs(input, 3))
    print(bs(input, 1))
    print(bs([], 100))