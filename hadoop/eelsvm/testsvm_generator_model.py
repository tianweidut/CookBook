# -*- coding: UTF-8 -*-
'''
Created on 2013-01-21

@author: tianwei
'''
import numpy as np

__author__ = "tianwei"
__date__ = "January 21 2013"
__description__ = "test svm step1 model generator"


def parse_testsvm_result(file_name):
    """
    parse the result of testsvm
    """
    f = open(file_name, "r")
    content = f.readlines()[0].split("\t")[1:]
    cnt = int(content[0])
    predict = float(content[1]) / float(cnt)
    f.close()

    return (cnt, predict)


def testsvm_generator(h, file_name):
    """
    Generate testsvm arguments from testsvm_step1.py program

    Inputs:
        h: input args
        file_name: the result from testsvm_step1.py

    Outputs:
        * means of predicted var
        * transform of input h
    """
    cnt, total_predict = parse_testsvm_result(file_name)

    h_trans = float(h) / float(np.sqrt(cnt))

    return (h_trans, total_predict)
