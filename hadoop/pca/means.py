
# -*- coding: UTF-8 -*-
'''
Created on 2012-12-19

@author: tianwei
'''
import dumbo
import numpy as np
import os


__author__ = "tianwei"
__date__ = "December 19  2012"
__description__ = "means matrix for the whole date set "

SEP = ','   #Parse from file

class Mapper():

    def __call__(self, data):
        """
        Mapper Program:Calculate the means of the matrix data set
        
        Inputs: 
            data, which is the whole split block data

        Outputs:
            key: column id of the matrix 
            value: means of this column

        """
        s = None
        cnt = 0     #cnt for items, it means rows cnt

        for docID,doc in data:
            for term in doc.split("\n"):
                point = np.fromstring(term,dtype=np.float64,sep=SEP)
                if s is None: 
                    s = np.array([0 for i in range(0,int(np.shape(point)[0]))])
                s = s + point 
                cnt = cnt + 1

        means = [float(element)/cnt for element in s]
        
        #output the dict for column id and the means value
        for i in range(0,len(means)):
           yield i, means[i]

class Reducer():
     
    def __call__(self,key,values):
        """
        Reducer Program: sum the different kinds of the column
        
        Inputs:
            key: column id
            values: means of this column 

        Outputs:
            key: column id
            values: all means of this column
        """
        cnt = 0
        means = 0.0
        for v in values:
            means = means + float(v)
            cnt = cnt + 1 

        yield key, float(means) / cnt

if __name__ == "__main__":
    dumbo.run(Mapper,Reducer)


