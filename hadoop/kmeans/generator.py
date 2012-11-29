# -*- coding: UTF-8 -*-
'''
Created on 2012-11-27

@author: tianwei
'''
import os
import sys
import random

FILEBLOCK = 100*100*10

data_path = "/home/hadoop/example/data"
sample_name = "sample_data" 
clusters_name = "clusters_data"

MIN = 0
MAX = 100000

class Generator(object):
    """
    """
    def __init__(self,kclusters=10, base=5, filesize=1, dim=2):
        """
        Args:
            kclusters --> the number of the clusters
            base --> calculate number
            filesize --> block of the file
            dim --> the dim of every single data item
        """
        self.kclusters = kclusters
        self.base = base 
        self.filesize = filesize 
        self.dim = dim

    def write(self,data):
        """
        every single data item
        """ 
        self.sample_file.write("\t".join(data))
        self.sample_file.write("\n")

    def writeClusters(self,data):
        """
        every single clusters
        """
        self.cluster_file.write("\t".join(data))
        self.cluster_file.write("\n")

    def run(self):
        """
        """
        self.sample_file = open(os.path.join(data_path,sample_name+str(self.kclusters)),"w")
        self.cluster_file = open(os.path.join(data_path,clusters_name+str(self.kclusters)),"w")
    
        #choice random number in [0,sum] 
        randomSeq = random.sample(xrange(0,self.filesize * FILEBLOCK * self.kclusters), self.kclusters)
        print randomSeq
    
        step = MAX / self.base
    
        cnt = 0
        for item in xrange(0,self.filesize * FILEBLOCK):
            for i in range(1,self.base+1):
                for j in range(1,self.base+1):
                    if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                        x = str(random.uniform(step *(i-1),step * i))
                        y = str(random.uniform(step *(j-1),step * j))
                        data = (x,y)
                        cnt = cnt +1 
                        if cnt in randomSeq:
                            self.writeClusters(data)

                        self.write(data)

        print "Finish generating the data"

        self.sample_file.close()
        self.cluster_file.close()


if __name__ == "__main__":
    from optparse import OptionParser
    parse  = OptionParser()
    
    parse.add_option("-d", "--dim", action="store", dest="dim", 
                        default=2, help="dim of the data")
    parse.add_option("-k","--kclusters",action = "store",dest = "kclusters",
            default = 10,help = "the number of the clusters")
    parse.add_option("-b","--base",action = "store",dest = "base", 
            default =5,help = "calculte number")
    parse.add_option("-s","--filesize",action = "store",dest = "filesize",
            default = 1,help = "filesize")

    (options, args) = parse.parse_args() 
    t = Generator(kclusters=options.kclusters, 
                  base=options.base,
                  filesize=options.filesize, 
                  dim=options.dim) 
    t.run()
