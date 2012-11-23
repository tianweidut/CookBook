# -*- coding: UTF-8 -*-
"""
    Hadoop hello world problem:
     Top 10 Problem
    We will use Dumbo
"""

import dumbo

def mapper(key,value):
    yield value.split(" ")[0],1

def reducer(key,values):
    yield key, sum(values)
    
def main():
    dumbo.run(mapper,reducer,combiner=reducer)

if __name__ == "__main__":
    main()
