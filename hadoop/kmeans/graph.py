# -*- coding: UTF-8 -*-
'''
Created on 2012-11-27

@author: tianwei
'''
import os
import sys
from matplotlib import pyplot 

SEP = "\t"

class GraphShow(object):
    def __init__(self,filepath):
        self.filepath = filepath

    def draw(self,data):
        """
        """
        if data == None:
            return
        data = data.strip("[").strip("]").strip("\n").split(SEP)
       # print data 
        self.ax.plot(float(data[0]),float(data[1]),linestyle='',marker='.')

    def run(self):
        """
        """
        self.init()
        reader = self.lineReader(self.filepath)
        line = reader.next()
        self.draw(line)
        cnt = 0
        while line:
            cnt = cnt + 1 
            if cnt > 100*100:
                break
            line = reader.next()
            self.draw(line)

        print "Finish the graph"
        
        pyplot.show()
        
        self.clear()
    
    def init(self):
        """
        """
        self.fig = pyplot.figure()
        self.ax = self.fig.add_subplot(111)

    def clear(self):
        pass

    def lineReader(self,filepath):
        """
        """
        f = open(filepath,"r")
        line = f.readline()
        while line:
            yield line
            line = f.readline() 

        f.close()
        yield None 


if __name__ == "__main__": 
    if len(sys.argv) !=2:
        filepath = "/home/hadoop/example/data/clusters_data10"
    else:
        filepath = sys.argv[1]

    g = GraphShow(filepath = filepath)
    g.run()
