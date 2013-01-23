# -*- coding: UTF-8 -*-
'''
Created on 2013-01-24

@author: tianwei
'''
import sys
from math import e

import numpy as np
import dumbo

__author__ = "tianwei"
__date__ = "December 24  2012"
__description__ = "varify the final result of MapReduce"

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
        self.SEP = None

    def get_sep(self, term):
        """
        """
        if "," in term:
            return ","
        else:
            return " "

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

    def varify(self, point):
        """
        varify the label
        """
        right_label = int(point[-1])
        point[-1] = 1

        point = np.dot(point, self.w_suffix_matrix)

        tmp = map(lambda x: 1 / (1 + pow(e, -x)), point.tolist())

        label = 1 if np.dot(tmp, self.w_matrix) - self.r > 0 else -1

        if label == 1:
            debug("1")
        else:
            debug("-1")
        return True if label == right_label else False

    def __call__(self, data):
        """
        Mapper Program 
        """

        true_cnt = 0
        false_cnt = 0

        for docID, doc in data:
            for term in doc.split("\n"):
                self.SEP = self.SEP if self.SEP is not None else self.get_sep(term)
                point = np.fromstring(term, dtype=np.float64, sep=self.SEP)
                if self.varify(point):
                    true_cnt = true_cnt + 1
                else:
                    false_cnt = false_cnt + 1

        debug(true_cnt)
        debug(false_cnt)
        yield "true_label", true_cnt
        yield "false_label", false_cnt


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

        if str(key) == "true_label":
            yield "true_label", sum(values)
        elif str(key) == "false_label":
            yield "false_label", sum(values)

if __name__ == "__main__":
    dumbo.run(Mapper, Reducer)
