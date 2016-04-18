#coding: utf-8

import math


def main():
    in_str = "abcd"
    combined_output(in_str)


def combined_output(in_str):
    len_str = int(len(in_str))
    nc = int(math.pow(2, len_str))

    for i in range(nc):
        output = ''
        for index, flag in enumerate([1 & (i >> m) for m in range(len_str + 1)]):
            if flag:
                output += in_str[index]

        print output


if __name__ == "__main__":
    main()
