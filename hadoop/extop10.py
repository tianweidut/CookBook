# -*- coding: UTF-8 -*-
"""
    Hadoop hello world problem:
     Top 10 Problem
    We will use Dumbo
"""

import dumbo

class  Mapper():
    def __init__(self):
        file = open("excludesIP.txt","r")
        self.excludes  = set(line.strip() for line in file)
        file.close()

    def __call__(self,key,value):
        ip = value.split("\t")[0] 
        if not ip in self.excludes:
            yield ip, 1

    def _call__(self,key,value):
        lines = value.split("\n")
        for line in lines:
            ip = line.split('\t')[0]
            if not ip in self.excludes:
                yield ip,1

class FilterMapper(object):
    """docstring for Filter Mapper"""
    def __init__(self):
        self.min = 1

    def __call__(self,key,value):
        if value > self.min:
            yield key,value

def reducer(key,values):
    yield key, sum(values)
    
def main():
    dumbo.run(Mapper,reducer,combiner=reducer)

def filterMain():
    job = dumbo.Job()
    job.additer(Mapper,reducer,combiner=reducer)    
    job.additer(FilterMapper,reducer,combiner=reducer)    
    job.run()

if __name__ == "__main__":
    #main()
    filterMain()
