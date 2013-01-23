# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import random

import numpy as np

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "generate w_matrix"

SEP = ','   # Parse from file


def generate_w_matrix(filename, dim, num):
    """
    generate the random 0-1 matrix
    """
    f = open(filename, "w")
    for i in range(0, dim):
        l = ",".join([str(random.uniform(-1, 1)) for j in range(0, num)])
        f.write(l + "\n")

    l = ",".join([str(random.uniform(0, 1)) for j in range(0, num)])
    f.write(l + "\n")

    f.close()

    print "------Finish generate w matrix------"


def read_w_matrix(filename):
    """
    """
    f = open(filename)
    content = f.readlines()

    matrix = None

    for line in content:
        point = np.fromstring(line, dtype=np.float64, sep=SEP)
        point = np.array([point])
        matrix = np.concatenate((matrix, point)) if matrix is not None else point

    f.close()

    return matrix
