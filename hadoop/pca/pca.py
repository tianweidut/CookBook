
# -*- coding: UTF-8 -*-
'''
Created on 2012-12-19

@author: tianwei
'''
import dumbo
import numpy as np
import sys


__author__ = "tianwei"
__date__ = "December 19  2012"
__description__ = "pca algorithm for the whole date set "

SEP = ','   #Parse from file

def debug(content,pos=None):
    print >> sys.stderr, "+"*15
    if pos is not None:print >> sys.stderr, pos
    print >> sys.stderr, content
    print >> sys.stderr, "-"*15

class Mapper():
    def __init__(self):
        """
        """
        self.means = self.load_means()

    def load_means(self):
        """
        load means from the file
        """
        f = open(self.params["means_filename"])
        content = f.readlines()
        matrix = [0.0 for i in content]

        for line in content:
            word = line.split("\t")
            matrix[int(word[0])] = float(word[1])
        
        f.close()

        return np.array(matrix)

    def standardization(self,matrix):
        """
        standardization the matrix
        """
        (rows, cols) = np.shape(matrix)
        new_matrix = np.zeros((rows,cols))
        std_matrix = np.std(matrix,0)
        
        for value in std_matrix:
            if value == 0: raise ZeroDivisionError, 'division by zero, cannot proceed'

        for row in range(rows):
            new_matrix[row,0:cols] =  matrix[row,0:cols] /std_matrix[row,0:cols]

        return new_matrix

    def __call__(self, data):
        """
        Mapper Program: 
        
        Inputs: 
            data, which is the whole split block data

        Outputs:
            key: untified id
            value: covariance
        """
        
        ###SETP1: calculate the means matrix 
        result = None

        for docID, doc in data:
            for term in doc.split("\n"):
                point = np.fromstring(term, dtype=np.float64, sep=SEP)
                point = np.array([point - self.means])
                result = np.concatenate((result, point)) if result is not None else point

        debug(result) 
        ###SETP2: normalize the matrix 
        #result = self.standardization(result)

        ###SETP3: for every column, calculate X(T) * X 
        local_matrix = np.transpose(result) * result

        yield 1, local_matrix

class Reducer():
     
    def __call__(self,key,values):
        """
        Reducer Program: generator eigenvalue
        
        Inputs:
            key: untified id
            values: covariance 

        Outputs:
            the sorted eigenvalue and eigenvector list 
        """
        s = None
        for v in values:
            if s is None : s = np.zeros(np.shape(v))  
            s = s + values

        yield s

if __name__ == "__main__":
    dumbo.run(Mapper)
    #dumbo.run(Mapper,Reducer)


