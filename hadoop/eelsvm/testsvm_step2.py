# -*- coding: UTF-8 -*-
'''
Created on 2013-01-21

@author: tianwei
'''
from math import e

import numpy as np
import dumbo

from common import get_sep, debug, generate_array

__author__ = "tianwei"
__date__ = "January 21 2012"
__description__ = "mapreduce test for el-svm, \
                   it will add a new value into last column"


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

    def extend_point(self, point):
        """
        Extent a new value into point array
        """
        point = np.resize(point, len(point) + 1)
        point[-1] = 1
        return point

    def __call__(self, data):
        """
        Mapper Program

            It will output the modified single line
        """

        for docID, doc in data:
            for term in doc.split("\n"):
                self.SEP = self.SEP if self.SEP is not None else get_sep(term)
                point = np.fromstring(term, dtype=np.float64, sep=self.SEP)
                label = int(point[-1])
                last_value = self.getDValue(point)
                point = self.extend_point(point)
                point[-1] = last_value
                point[-2] = float(label)
                output = ",".join([str(i) for i in point])
                yield output, "\t"

if __name__ == "__main__":
    dumbo.run(Mapper)
