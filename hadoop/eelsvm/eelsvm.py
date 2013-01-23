# -*- coding: UTF-8 -*-
'''
Created on 2013-01-21

@author: tianwei
'''
import sys
from math import e
from math import pi

import numpy as np
import dumbo

__author__ = "tianwei"
__date__ = "January 21 2013"
__description__ = "eel-svm for the whole splited block data, \
                   It will use the modified dataseti and the arguments"

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


class Mapper():
    def __init__(self):
        """
        """
        self.h = float(self.params["h_trans"])
        self.means = float(self.params["means"])
        self.a = 1.0 / float(np.sqrt(2 * pi))
        self.w_matrix = load_w_matrix(self.params["w_matrix_filename"])
        self.SEP = None

    def get_sep(self, term):
        """
        """
        if "," in term:
            return ","
        else:
            return " "

    def get_predict_value(self, v):
        """
        predict value from v by formula
        """
        u = float(self.means - v) / float(self.h)
        u2 = 0 - 0.5 * np.power(u, 2)
        p = self.a * np.power(e, u2)

        return p

    def calculate(self, point):
        """
        Calculate Program

        Inputs:
            point, a single-original line data

        Outputs:
            localH: a(T) * a
            localD: a * y
        """
        # the label of original dataset
        y = int(point[-2])
        # argument var from testsvm_step2
        argument = float(point[-1])
        # change the label
        point[-2] = 1
        # shorten the point array
        point = np.array(point[:-1])
        # calculate the array
        point = np.dot(point, self.w_matrix)
        point_list = map(lambda x: 1 / (1 + pow(e, -x)), point.tolist())
        point = np.array(point_list + [-1], dtype=np.float64)
        point.shape = (1, int(np.shape(point)[0]))
        # get the argument of pi
        argument_pi = self.get_predict_value(argument)

        return (np.dot(point.T, point) * argument_pi,
                y * point.T * argument_pi)

    def __call__(self, data):
        """
        Mapper Program:

        Inputs:
            data, which is the whole split block data

        Outputs:
            key: untified id
            value: resultD,resultH
        """

        # SETP1: read data matrix and do some transpose
        resultH = None
        resultD = None

        for docID, doc in data:
            for term in doc.split("\n"):
                self.SEP = self.SEP if self.SEP is not None else self.get_sep(term)
                point = np.fromstring(term, dtype=np.float64, sep=self.SEP)
                (localH, localD) = self.calculate(point)

                if resultH is not None:
                    resultH = resultH + localH
                    resultD = resultD + localD
                else:
                    resultH = localH
                    resultD = localD

        debug(np.shape(resultH))
        debug(np.shape(resultD))

        yield "nonused", (resultD.tolist(), resultH.tolist())


class Reducer():

    def __init__(self):
        """
        """
        self.w_matrix = load_w_matrix(self.params["w_matrix_filename"])

    def __call__(self, key, values):

        """
        Reducer Program: generate the model arguments

        Inputs:
            key: untified id
            values: resultD and resultH

        Outputs:
            model arguments
        """
        globalD = None
        globalH = None

        for value in values:
            debug(np.shape(value[1]))
            debug(np.shape(value[0]))
            globalD = globalD + np.array(value[0]) if globalD is not None else np.array(value[0])
            globalH = globalH + np.array(value[1]) if globalH is not None else np.array(value[1])

        debug("global")
        debug(np.shape(globalH))
        debug(np.shape(globalD))

        yield "nonused", (globalD.tolist(), globalH.tolist())


if __name__ == "__main__":
    dumbo.run(Mapper, Reducer, Reducer)
