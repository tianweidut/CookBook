# -*- coding: UTF-8 -*-
'''
Created on 2013-01-23

@author: tianwei
'''
import sys
from math import e

import numpy as np

__author__ = "tianwei"
__date__ = "January 23 2013"
__description__ = "common lib for mapreduce"

SEP_local = ","


def debug(content, pos=None):
    print >> sys.stderr, "+" * 15
    if pos is not None:
        print >> sys.stderr, pos
    print >> sys.stderr, content
    print >> sys.stderr, "-" * 15


def load_w_matrix(filename):
    """
    load means from the file
    """
    f = open(filename)
    content = f.readlines()

    matrix = None

    for line in content:
        point = np.fromstring(line, dtype=np.float64, sep=SEP_local)
        point = np.array([point])
        matrix = np.concatenate((matrix, point)) if matrix is not None else point

    f.close()

    return matrix


def get_sep(term):
        """
        """
        if "," in term:
            return ","
        else:
            return " "
