# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
from math import e

import numpy as np
import dumbo

from common import debug, get_sep
from common import generate_array
from common import TRUE_T, TRUE_F
from common import FALSE_T, FALSE_F
from common import TRUE_T_STR, TRUE_F_STR
from common import FALSE_T_STR, FALSE_F_STR

__author__ = "tianwei"
__date__ = "December 24  2012"
__description__ = "mapreduce test for el-svm"


class Mapper():
    def __init__(self):
        """
        """
        self.SEP = None
        self.load_models()

    def load_models(self):
        """
        load models from the file
        """
        f = open(self.params["models_filename"])
        content = f.readlines()
        content = content[0].strip('\n').split('\t')

        self.w_suffix_matrix = generate_array(content[2],
                                              element_type=np.float64)

        self.w_matrix = generate_array(content[4],
                                       element_type=np.float64)
        self.w_matrix = np.transpose(self.w_matrix)

        f.close()

    def varify(self, point):
        """
        varify the label
        """
        right_label = int(point[-1])
        point[-1] = 1

        point = np.dot(point, self.w_suffix_matrix)

        tmp = map(lambda x: 1 / (1 + pow(e, -x)), point.tolist())

        label = 1 if np.dot(tmp, self.w_matrix) > 0 else -1

        if right_label == 1:
            return TRUE_T if label == right_label else FALSE_T
        elif right_label == -1:
            return TRUE_F if label == right_label else FALSE_F

    def __call__(self, data):
        """
        Mapper Program
        """

        true_cnt_t = 0
        true_cnt_f = 0
        false_cnt_t = 0
        false_cnt_f = 0

        for docID, doc in data:
            for term in doc.split("\n"):
                self.SEP = self.SEP if self.SEP is not None else get_sep(term)
                point = np.fromstring(term, dtype=np.float64, sep=self.SEP)
                result = self.varify(point)
                if result == TRUE_F:
                    true_cnt_f = true_cnt_f + 1
                elif result == TRUE_T:
                    true_cnt_t = true_cnt_t + 1
                elif result == FALSE_F:
                    false_cnt_f = false_cnt_f + 1
                elif result == FALSE_T:
                    false_cnt_t = false_cnt_t + 1

        yield TRUE_T_STR, true_cnt_t
        yield TRUE_F_STR, true_cnt_f
        yield FALSE_T_STR, false_cnt_t
        yield FALSE_F_STR, false_cnt_f


class Reducer():
    def __call__(self, key, values):
        """
        Reducer Program: statistical for elsvm

        Inputs:
            key: true_label or false_label
            values: cnt for label

        Outputs:
            the statistical result
        """

        if str(key) == TRUE_T_STR:
            yield TRUE_T_STR, sum(values)
        elif str(key) == TRUE_F_STR:
            yield TRUE_F_STR, sum(values)
        elif str(key) == FALSE_T_STR:
            yield FALSE_T_STR, sum(values)
        elif str(key) == FALSE_F_STR:
            yield FALSE_F_STR, sum(values)

if __name__ == "__main__":
    dumbo.run(Mapper, Reducer)
