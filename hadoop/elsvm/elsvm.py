# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import sys
from math import e

import numpy as np
import dumbo

from debug import debug

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "el-svm for the whole splited block data"

SEP = ','   # Parse from file


def load_w_matrix(filename):
    """
    load means from the file
    """
    f = open(filename)
    content = f.readlines()

    matrix = None

    for line in content:
        point = np.fromstring(line, dtype=np.float64, sep=SEP)
        point = np.array([point])
        matrix = np.concatenate((matrix, point)) if matrix is not None else point

    f.close()

    debug(matrix)
    return matrix


class Mapper():
    def __init__(self):
        """
        """
        self.w_matrix = load_w_matrix(self.params["w_matrix_filename"])

    def calculate(self, point):
        """
        Calculate Program

        Inputs:
            point, a single-original line data

        Outputs:
            localH: a(T) * a
            localD: a * y
        """
        y = int(point[-1])
        point[-1] = 1
        point = np.dot(point, self.w_matrix)
        point_list = map(lambda x: 1 / (1 + pow(e, -x)), point.tolist())
        point = np.concatenate((np.array(point_list), np.array([-1])))

        return (np.dot(np.transpose(point), point), y * point)

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
                point = np.fromstring(term, dtype=np.float64, sep=SEP)
                (localH, localD) = self.calculate(point) 
                if resultH is not None:
                    resultH = resultH + localH
                    resultD = resultD + localD
                else:
                    resultH = localH
                    resultD = localD

        yield 1, (resultD.tolist(), resultH.tolist())


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
            globalH = globalH + value[1] if globalH is not None else value[1]
            globalD = globalD + value[0] if globalD is not None else value[0]
        
        eye_matrix = np.eye(int(self.params["num"]) + 1) / \
                            int(self.params["v"])

        result_matrix = np.dot(np.linalg.inv(globalH + eye_matrix), globalD)

        result_matrix = np.transpose(result_matrix)

        yield globalH, globalD, \
                self.w_matrix.tolist(), \
                result_matrix[-1].tolist(), self.params["num"],  \
                result_matrix[:-1].tolist(), self.params["v"]
        

if __name__ == "__main__":
    dumbo.run(Mapper, Reducer)
