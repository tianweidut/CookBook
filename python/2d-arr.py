#coding: utf-8

def main():
    print '--error 2d array'
    array = [[0] * 3] * 3
    print array
    array[0][1] = 1
    print array

    for i in range(3):
        print "array[%s][1]" % i, id(array[i][1]), array[i][1]

    print '--right 2d array'
    array = [[0 for i in range(3)] for j in range(3)]
    print array
    array[0][1] = 1
    print array

    print '--right 2d array'
    array = [[0] * 3 for j in range(3)]
    print array
    array[0][1] = 1
    print array


if __name__ == "__main__":
    main()
