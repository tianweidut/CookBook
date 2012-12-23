# -*- coding: UTF-8 -*-
'''
Created on 2012-12-23

@author: tianwei
'''
import numpy as np
import dumbo

from debug import debug

__author__ = "tianwei"
__date__ = "December 23 2012"
__description__ = "use pca result to filter the whole blocked matrix"

SEP = ','   # Parse from file


class Mapper():
    def __init__(self):
        """
        """
        self.dims = int(self.params["dims"])
        self.filter_matrix = self.load_filter_matrix()

    def load_filter_matrix(self):
        """
        load filter matrix from the file
        """
        f = open(self.params["filter_filename"])
        content = f.readlines()
        
        matrix = None
        for i in range(0, self.dims):
            term = (content[i].split("\t")[1]).strip("[").strip("]")
            point = np.fromstring(term, dtype=np.float64, sep=SEP)
            point = np.array([point])
            matrix = np.concatenate((matrix, point)) if matrix is not None else point

        f.close()
        
        return np.transpose(matrix)

    def __call__(self, key, value):
        """
        Mapper Program: 
        
        Inputs: 
            key,value, which is the whole split block data

        Outputs:
            the calculted matrix
        """
        point = np.fromstring(value, dtype=np.float64, sep=SEP)
        result = np.dot(point, self.filter_matrix)

        yield result

if __name__ == "__main__":
    dumbo.run(Mapper)
