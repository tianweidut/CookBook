# -*- coding: UTF-8 -*-
'''
Created on 2012-12-26

Updated on 2013-01-13

@author: tianwei
'''
import math
import numpy as np

from w_matrix import read_w_matrix

__author__ = "tianwei"
__date__ = "December 26 2012"
__description__ = "generate model args from map-reduce dump file, \
                    the new version support increment model"

SEP = ","

history_globalH = None
history_globalD = None


def generate_array(string_list, element_type):
        """
        generate narray from string list
        """
        matrix = None
        whole_list = string_list.strip("[").strip("]").split("],")
        for s in whole_list:
            s = s.replace("[", " ").replace("]", " ").strip(" ")
            s = np.array([np.fromstring(s, dtype=element_type, sep=SEP)]) 
            matrix = np.concatenate((matrix, s)) \
                    if matrix is not None else s

        return matrix


def read_matrix(f):
    """
    read matrix from file, to globalD, globalH
    """
    content = f.readline().split("\t")
    globalD = content[1].strip("\n")
    globalH = content[2].strip("\n")

    globalD = generate_array(globalD, element_type=np.float64)
    globalH = generate_array(globalH, element_type=np.float64)

    return (globalD, globalH)


def generate_model(input_filename, output_filename,
                    w_matrix_filename=None, 
                    num=20, v=100,
                    is_increment=False,
                    a_inc=None):
    """
    generate models args from dump file
    we can also import increment model

    Args:
        a_inc : args of a
        is_increment: whether increment model or not
    """
    fin = open(input_filename, "r")
    fout = open(output_filename, "w")

    w_matrix = read_w_matrix(w_matrix_filename)

    (globalD, globalH) = read_matrix(fin)
    print np.shape(globalH)
    print np.shape(globalD)

    # According to the model selection(whether increment or not)
    # decide how to generate model
    if is_increment:
        # here, we will use increment mode to update globalH and globalD.
        (globalH, globalD) = update_increment_model(globalH, globalD, a_inc)
    
    # update H and D
    global history_globalD
    global history_globalH
    history_globalH = globalH
    history_globalD = globalD

    eye_matrix = np.eye(int(num) + 1) / int(v)

    result_matrix = np.dot(np.linalg.inv(globalH + eye_matrix), globalD)
    result_matrix.shape = (int(np.shape(result_matrix)[0]), 1)
    result_matrix = result_matrix.T

    print>>fout, globalH.tolist(), '\t',
    print>>fout, globalD.tolist(), '\t',
    print>>fout, w_matrix.tolist(), '\t',
    print>>fout, result_matrix[0, -1].tolist(), '\t',
    print>>fout, num, '\t',
    print>>fout, result_matrix[0, :-1].tolist(), '\t',
    print>>fout, v

    fin.close()
    fout.close()

    return output_filename


def update_increment_model(local_globalH, local_globalD, a_inc):
    """
    update increment model
    """
    global history_globalD
    global history_globalH

    if history_globalD is None and history_globalH is None:
        return (local_globalH, local_globalD)

    local_globalH = math.sqrt(a_inc) * history_globalH + local_globalH
    local_globalD = a_inc * history_globalD + local_globalD

    return (local_globalH, local_globalD)


def test():
    """
    """
    generate_model(input_filename="/home/hadoop/example/elsvm/result/el_svm.csv",
            output_filename="/home/hadoop/example/elsvm/result/el_svm2.csv",
            w_matrix_filename='/home/hadoop/example/elsvm/result/w_matrix_file')

if __name__ == "__main__":
    test()
