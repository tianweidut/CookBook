

def odd(l, r):
    if l > r:
        l, r = r, l

    ret = []
    
    for i in range(l, r + 1):
        if i <= 0 or i % 2 == 0:
            continue
        else:
            ret.append(i)

    return ret


if __name__ == "__main__":
    print odd(1,3)
    print odd(0, 5)
    print odd(9, 5)
    print odd(2, 5)
