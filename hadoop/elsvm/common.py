# -*- coding: UTF-8 -*-
'''
Created on 2013-01-23

@author: tianwei
'''
import sys

import numpy as np

__author__ = "tianwei"
__date__ = "January 23 2013"
__description__ = "common lib for mapreduce"

SEP_local = ","


# Constant for varify label
TRUE_T = 0
TRUE_F = 1
FALSE_T = 2
FALSE_F = 3

TRUE_T_STR = "true_cnt_t"
TRUE_F_STR = "true_cnt_f"
FALSE_T_STR = "false_cnt_t"
FALSE_F_STR = "false_cnt_f"


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


def generate_array(string_list, element_type):
        """
        generate narray from string list
        """
        matrix = None
        whole_list = string_list.strip("[").strip("]").split("],")
        for s in whole_list:
            s = s.replace("[", " ").replace("]", " ").strip(" ")
            s = np.array([np.fromstring(s, dtype=element_type, sep=SEP_local)])
            matrix = np.concatenate((matrix, s)) \
                     if matrix is not None else s

        return matrix
