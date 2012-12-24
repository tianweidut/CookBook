# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import os
import sys
from random import randint

import numpy as np
import dumbo

from debug import debug

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "main-wrapper for elsvm"

SEP = ','   # Parse from file
HADOOP_PATH = os.environ["HADOOP_HOME"]


def main():
    """
    Main wrapper
    """

class Parse():
    def __call__(self):
        """
        Opt Parse for command line 
    
        Inputs:
            None

        Outputs:
            options:
            args:
        """
        from optparse import OptionParser
        parse = OptionParser()
        parse.add_option("-o", "--openHadoop", action="store_true", dest="is_hadoop", 
                        help="whether it is running on hadoop platform")
        parse.add_option("-c", "--closeHadoop", action="store_false", dest="is_hadoop", 
                        help="whether it is running on hadoop platform")
        parse.add_option("-n", "--num", action="store", dest="num", 
                        help="num for elsvm")
        parse.add_option("-v", "--varibles", action="store", dest="var",
                        help="v for elsvm")
        parse.add_option("-s", "--sampleName", action="store", dest="sample_name",
                        default="elsvm_data.csv", help="sample for elsvm")
        parse.add_option("-p", "--path", action="store", dest="path",
                        help="sample data path")
        parse.add_option("-t", "--output_path", action="store", dest="output_path",
                        help="result output path")
        parse.add_option("-o", "--output_name", action="store",
                        dest="output_name",
                        help="output name")
        parse.add_option("-d", "--dim", action="store", dest="dim",
                        help="dim number for sample data")
        
        (options, args) = parse.parse_args()

        if len(sys.argv) < 2:
            print "Usages:"
            print "-o --openHadoop Open Hadoop Platform"
            print "-c --closeHadoop use dumbo local environment"
            print "-p --dataPath source sample data path"
            print "-n --num for el-svm "
            print "-d --dim for sample data "
            print "-v --v(var) for el-svm"
            print "-s --sampleName sample Name "
            print "please enjoy! From tianwei *_* "
        return (None, None)


class ElsvmWrapper():
    """
    """
    exe_dir = os.path.abspath(os.path.dirname(__file__))
    exe_elsvm = os.path.join(exe_dir, "elsvm.py")
    exe_test = os.path.join(exe_dir, "testsvm.py") 
    model_args = os.path.join(exe_dir, "model.csv")

    def __init__(self, is_hadoop, data_path, output_path,
            n=100, dim=2, v=100,
            sample_name="elsvm_data.csv",
            output_name="elsvm_output.csv"):
        """
        """
        self.is_hadoop = is_hadoop
        self.data_path = data_path
        self.n = n
        self.dim = dim
        self.v = v
        self.sample_name = sample_name
        self.w_matrix_filename = os.path.join(self.exe_dir, "w_matrix_file")
        self.output_name = output_name
        self.output_path = output_path

    def generate_w_matrix(self):
        """
        generate the random 0-1 matrix
        """
        f = open(self.w_matrix_filename, "w")   
        for i in range(0, self.dim + 1):
            l = ",".join([str(randint(-1, 1)) for j in range(0, self.num)])
            print l
            f.write(l + "\n")

        f.close()

        print "Finish generate w matrix"

    def mapreduce(self):
        """
        mapreduce in hadoop
        """
        # STEP1: dumbo main start
        args = " dumbo start " + self.exe_elsvm      
        if self.is_hadoop:
            args += " - hadoop " + HADOOP_PATH 

        args += " -input " + os.path.join(self.data_path, self.sample_name)
        args += " -output " + os.path.join(self.output_path, self.output_name)
 
        args += " -param v='%s' " % (self.v)
        args += " -param num='%s' " % (self.num)
        args += " -overwrite yes "

        if self.is_hadoop:
            args += " -file " + self.w_matrix_filename
            args += " -param w_matrix_filename='%s' " % \
                (os.path.basename(self.w_matrix_filename))
        else:
            args += " -param w_matrix_filename='%s' " % \
                (self.w_matrix_filename)

        print args
        ret = os.system(args)
        if ret != 0:
            raise ValueError("EL-SVM process error!")
        else:
            print "------Finish the EL-SVM training process ----"
        
        # STEP2: dump output 
        if self.ishadoop:
            print "------Now we dump the output ------"
            
            args = ""
            args += " dumbo cat "
            args += os.path.join(self.output_path, self.output_name)
            args += " -hadoop " + HADOOP_PATH
            args += " > " + self.model_args

            print args 

            ret = os.system(args)

            if ret != 0:
                raise ValueError("Dump process failed!")
            else:
                print "-----finish the dump process-----"

            result_name = self.model_args
        else:
            result_name = os.path.join(self.output_path, self.output_name)
        
        return result_name

    def test(self):
        """
        """
        pass

    def run(self):
        """
        """
        # STEP1: generate random matrix w
        self.generate_w_matrix()

        # STEP2: map-reduce
        result_name = self.mapreduce()

        # STEP3: test for mapreduce
        self.test(result_name)

if __name__ == "__main__":
    (options, args) = Parse()
    e = ElsvmWrapper(
            is_hadoop=options.is_hadoop,
            data_path=options.path,
            n=options.num,
            v=options.var,
            dim=options.dim,
            output_name=options.output_name,
            output_path=options.output_path,
            sample_name=options.sample_name)
    e.run() 

