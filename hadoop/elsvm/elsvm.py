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


class Mapper():
    def __init__(self):
        """
        """
        self.w_matrix = self.load_w_matrix()

    def load_w_matrix(self):
        """
        load means from the file
        """
        f = open(self.params["w_matrix_filename"])
        content = f.readlines()

        matrix = None

        for line in content:
            point = np.fromstring(line, dtype=np.float64, sep=SEP)
            point = np.array([point])
            matrix = np.concatenate((matrix, point)) if matrix is not None else point

        f.close()

        return matrix

    def calculate(self, point):
        """
        Calculate Program

        Inputs:
            point, a single-original line data

        Outputs:
            localH: a(T) * a
            localD: a * y
        """
        y = np.array([point[-1]])
        point[-1] = 1
        point = np.dot(point, self.w_matrix)
        point_list = map(lambda x: 1 / (1 + pow(e, -x)), point.tolist())
        point = np.concatenate((np.array(point_list), np.array([1])))

        return (np.dot(np.transpose(point), point), np.dot(y, point))

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
                
        yield resultD, resultH

class Reducer(): 
    def __call__(self, key, values):
        """
        Reducer Program: generator eigenvalue
        
        Inputs:
            key: untified id
            values: covariance 

        Outputs:
            the sorted eigenvalue and eigenvector list 
        """
        

if __name__ == "__main__":
    dumbo.run(Mapper, Reducer)
