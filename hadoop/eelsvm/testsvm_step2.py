# -*- coding: UTF-8 -*-
'''
Created on 2013-01-21

@author: tianwei
'''
import sys
from math import e

import numpy as np
import dumbo

__author__ = "tianwei"
__date__ = "January 21 2012"
__description__ = "mapreduce test for el-svm, \
                   it will add a new value into last column"

SEP = ' '   # Parse from file
SEP_local = ','   # Parse from file


def debug(content, pos=None):
    print >> sys.stderr, "+" * 15
    if pos is not None:
        print >> sys.stderr, pos
    print >> sys.stderr, content
    print >> sys.stderr, "-" * 15


class Mapper():
    def __init__(self):
        """
        """
        self.load_models()

    def generate_array(self, string_list, element_type):
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

    def load_models(self):
        """
        load models from the file
        """
        f = open(self.params["models_filename"])
        content = f.readlines()
        content = content[0].strip('\n').split('\t')

        self.w_suffix_matrix = self.generate_array(content[2],
                                                   element_type=np.float64)
        self.r = float(content[3])

        self.w_matrix = self.generate_array(content[5],
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
                point = np.fromstring(term, dtype=np.float64, sep=SEP)
                label = int(point[-1])
                last_value = self.getDValue(point)
                point = self.extend_point(point)
                point[-1] = last_value
                point[-2] = float(label)
                output = ",".join([str(i) for i in point])
                yield output, "\t"

if __name__ == "__main__":
    dumbo.run(Mapper)
