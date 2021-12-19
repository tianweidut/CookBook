#coding: utf-8

import math


def main():
    in_str = "abcd"
    combined_output(in_str)
    combined_output_k(n=4, k=2)


def combined_output(in_str):
    len_str = int(len(in_str))
    nc = int(math.pow(2, len_str))

    for i in range(nc):
        output = ''
        for index, flag in enumerate([1 & (i >> m) for m in range(len_str + 1)]):
            if flag:
                output += in_str[index]

        print output


def combined_output_k(n, k):
    nc = int(math.pow(2, n))
    ret = []

    for i in range(nc):
        output = []
        for index, flag in enumerate([1 & (i >> m) for m in range(n + 1)]):
            if flag:
                output.append(index + 1)

        if len(output) == k:
            ret.append(output)

    print ret

if __name__ == "__main__":
    main()
