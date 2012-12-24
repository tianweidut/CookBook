# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import os
import sys

from dumbo import cmd, util
from dumbo.util import Options

__author__ = "tianwei"
__date__ = "Dec 24  2012"
__description__ = "Main wraper for PCA"

# Hadoop Configure
HADOOP_PATH = os.environ["HADOOP_HOME"]


class Control(object):
    """
    Kmeans Control Class Logical
    """
    exDir = os.path.abspath(os.path.dirname(__file__))
    means_step1 = os.path.join(exDir, "means.py")
    pca_step2 = os.path.join(exDir, "pca.py")
    filter_step3 = os.path.join(exDir, "filter.py")

    def __init__(self,
            ishadoop=False, 
            dataPath=None,
            localPath=None, 
            sampleName="data.csv"):

        self.ishadoop = ishadoop 
        self.sampleName = sampleName
        self.localPath = localPath

        if self.ishadoop:
            self.dataDir = dataPath
            self.patialSource = os.path.join(self.localPath,self.clusterData)
        else:
            self.dataDir = os.path.join(dataPath,"data") 
            self.patialSource = os.path.join(self.dataDir,self.clusterData)

        self.resultDir = os.path.join(self.dataDir,'result')
        self.sourceData = os.path.join(self.dataDir,self.sampleName)

    def setup(self):
        """
        Initial setup code
        """
        
        if self.ishadoop:
            return
        #delete the results file
        for f in os.listdir(self.resultDir):
            name = os.path.join(self.resultDir,f)
            try:
                os.remove(name)
            except:
                pass

    def clean(self):
        """
        clean the resource 
        """
        self.tmpFile.close() 

    def run(self):
        """
        """
        self.setup()
        
        self.jobRun()

        self.clean()

    def jobRun(self, inputfile=None, clusterfile=None, outputfile=None):
        """
        every map-reduce job

        Args:
            inputfile: clusterfile of this stage
            outputfile : patial result , which need to be calculated for
            distance to end kmeans calculate process
        """
       
        args = " dumbo start " + self.exProgram
        if self.ishadoop:
            args += " -hadoop " + HADOOP_PATH
        
        args += " -input " + inputfile
        args += " -output " + outputfile 
        
        if self.ishadoop:
            args += " -file " + clusterfile
            args += ' -param filename="%s" '%(os.path.basename(clusterfile))
            args += ' ishadoop="yes" ' 
            args += " -overwrite yes "
        else:
            args += " -param filename=" + clusterfile
            args += ' ishadoop ="no" ' 

        print args 
        
        ret = os.system(args)
        if ret != 0 :
            raise ValueError("Calculate Error!")
        else:
            print "----Finish the calculate process ----"
        
        if self.ishadoop:
            print "------Now we dump the output ------"
            
            resultName =  os.path.join(self.localPath,os.path.basename(outputfile))

            args = ""
            args += " dumbo cat "
            args += outputfile
            args += " -hadoop " + HADOOP_PATH
            args += " > " + resultName

            print args 

            ret = os.system(args)

            if ret != 0:
                raise ValueError("Dump process failed!")
            else:
                print "-----finish the dump process-----"
        else:
            resultName = outputfile

        return resultName 

def main(argv):
    """
    main thread
    """
    from optparse import OptionParser
    parse = OptionParser()
    
    parse.add_option("-o", "--openHadoop", action="store_true", dest="ishadoop", 
                     help="whether it is running on hadoop platform")
    parse.add_option("-q", "--closeHadoop", action="store_false", dest="ishadoop", 
                     help="whether it is running on hadoop platform")
    parse.add_option("-d", "--dataPath", action="store", dest="dataPath",
                     help = "source sample data path")
    parse.add_option("-l","--localPath",action = "store",dest = "localPath",default = None, 
            help = "clusters file path which is in the local path and carrying with python program")
    parse.add_option("-s","--simpleName",action = "store",dest = "sampleName",
            default ="data.csv" ,help = "sample name")
    parse.add_option("-c","--clusterName",action = "store",dest = "clusterName",
            default ="clusters.csv" ,help = "cluster name")

    (options, args) = parse.parse_args() 
 
    if len(sys.argv) < 2:
        print "Usages:"
        print "-o --openHadoop Open Hadoop Platform"
        print "-q --closeHadoop use dumbo local environment"
        print "-d --dataPath source sample data path"
        print "-l --localPath clusters file path which is in the local path and carrying with python program "
        print "-s --simpleName sample Name "
        print "-c --clusterName cluster Name"
        print "please enjoy! From tianwei *_* "
        return 
    
    print options.ishadoop
    print bool(options.ishadoop)
    k = KmeansControl(ishadoop=options.ishadoop,
                        dataPath = options.dataPath,
                        localPath = options.localPath,
                        clusterName = options.clusterName,
                        sampleName = options.sampleName)
    k.run()

if __name__ == "__main__":
    main(sys.argv)
