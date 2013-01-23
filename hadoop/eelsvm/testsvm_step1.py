# -*- coding: UTF-8 -*-
'''
Created on 2013-01-21

@author: tianwei
'''
from math import e

import numpy as np
import dumbo

from common import debug, load_w_matrix, get_sep
from common import generate_array

__author__ = "tianwei"
__date__ = "January 21 2013"
__description__ = "mapreduce test for el-svm, non 1 or -1, \
                   get count and means from the origianl data"

SEP_local = ','   # Parse from file


class Mapper():
    def __init__(self):
        """
        """
        self.load_models()
        self.SEP = None

    def load_models(self):
        """
        load models from the file
        """
        f = open(self.params["models_filename"])
        content = f.readlines()
        content = content[0].strip('\n').split('\t')

        self.w_suffix_matrix = generate_array(content[2],
                                              element_type=np.float64)
        self.r = float(content[3])

        self.w_matrix = generate_array(content[5],
                                       element_type=np.float64)
        self.w_matrix = np.transpose(self.w_matrix)

        f.close()

    def getDValue(self, point):
        """
        get the D-value of the label
        """
        point[-1] = 1

        point = np.dot(point, self.w_suffix_matrix)

        tmp = map(lambda x: 1 / (1 + pow(e, -x)), point.tolist())

        # use D-value directly
        label_d_value = float(np.dot(tmp, self.w_matrix) - self.r)

        return label_d_value

    def __call__(self, data):
        """
        Mapper Program
        """

        cnt = 0
        means = 0.0

        for docID, doc in data:
            for term in doc.split("\n"):
                self.SEP = self.SEP if self.SEP is not None else get_sep(term)
                point = np.fromstring(term, dtype=np.float64, sep=self.SEP)
                means += self.getDValue(point)
                cnt = cnt + 1

        yield "nonused", (cnt, means)


class Reducer():
    def __call__(self, key, values):
        """
        Reducer Program: statistical for the partial result of elsvm

        Inputs:
            key: true_label or false_label
            values: cnt for label
        Outputs:
            cnt: sum of local lines
            means: means of local means
        """

        local_cnt = 0
        local_means = 0.0

        for value in values:
            local_cnt += int(value[0])
            local_means += float(value[1])

        yield "nonused", (local_cnt, local_means)

if __name__ == "__main__":
    dumbo.run(Mapper, Reducer, Reducer)
