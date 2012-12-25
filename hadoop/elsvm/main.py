# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import os
import sys
import random

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "main-wrapper for elsvm"

SEP = ','   # Parse from file
HADOOP_PATH = os.environ["HADOOP_HOME"]


class Parse():
    def run(self):
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
        parse.add_option("-m", "--output_name", action="store",
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

        return (options, args)


class ElsvmWrapper():
    """
    """
    exe_dir = os.path.abspath(os.path.dirname(__file__))
    exe_elsvm = os.path.join(exe_dir, "elsvm.py")
    exe_test = os.path.join(exe_dir, "testsvm.py") 
    
    output_test = "output_test.csv"

    def __init__(self, is_hadoop, data_path, output_path,
            n=100, dim=2, v=100,
            sample_name="elsvm_data.csv",
            output_name="elsvm_output.csv"):
        """
        """
        self.is_hadoop = is_hadoop
        self.data_path = data_path
        self.num = int(n)
        self.dim = int(dim)
        self.v = int(v)
        self.sample_name = sample_name
        self.output_name = output_name
        self.output_path = output_path
        self.w_matrix_filename = os.path.join(self.output_path, "w_matrix_file")

    def generate_w_matrix(self):
        """
        generate the random 0-1 matrix
        """
        f = open(self.w_matrix_filename, "w")   
        for i in range(0, self.dim):
            l = ",".join([str(random.uniform(-1, 1)) for j in range(0, self.num)])
            f.write(l + "\n")

        l = ",".join([str(random.uniform(0, 1)) for j in range(0, self.num)])
        f.write(l + "\n")

        f.close()

        print "------Finish generate w matrix------"
    
    def mapreduce_routine(self, exe_program,input_file, output_file,
            access_args="",
            content=""):
        """
        """
        args = " dumbo start " + exe_program      
        if self.is_hadoop:
            args += " -hadoop " + HADOOP_PATH 

        args += " -input " + input_file
        args += " -output " + output_file
        args += " -overwrite yes "
        args += access_args
         
        print args
        print "+++In map-reduce phase+++"
        ret = os.system(args)

        if ret != 0:
            raise ValueError("%s process error!"%(content))
        else:
            print "---------Finish the %s process --------"%(content)

    def cat_routine(self, input_file, output_file):
        """
        """
        print "------Now we dump the output ------"

        args = ""
        args += " dumbo cat "
        args += input_file
        args += " -hadoop " + HADOOP_PATH

        args += " > " + output_file

        print args 

        ret = os.system(args)

        if ret != 0:
            raise ValueError("Dump process failed!")
        else:
            print "-----finish the dump process-----"

    def mapreduce(self):
        """
        mapreduce in hadoop
        """
        # STEP1: dumbo main start
        access_args = " -param v='%s' " % (self.v)
        access_args += " -param num='%s' " % (self.num)
        
        if self.is_hadoop:
            access_args += " -file " + self.w_matrix_filename
            access_args += " -param w_matrix_filename='%s' " % \
                (os.path.basename(self.w_matrix_filename))
        else:
            access_args += " -param w_matrix_filename='%s' " % \
                (self.w_matrix_filename)

        self.mapreduce_routine(exe_program=self.exe_elsvm,
                    input_file=os.path.join(self.data_path, self.sample_name),
                    output_file=os.path.join(self.output_path, self.output_name),
                    access_args=access_args,
                    content="EL-SVM MapReduce Process")
        
        # STEP2: dump output 
        self.model_args = os.path.join(self.output_path, self.output_name)
        if self.is_hadoop:
            self.cat_routine(
                    input_file=os.path.join(self.output_path, self.output_name), 
                    output_file=self.model_args)

        return self.model_args

    def test(self, models_name):
        """
        """
        # STEP1: dumbo main start
        access_args = " -param models_filename='%s' " % \
            os.path.join(self.output_path, self.output_name)
        access_args += " -overwrite yes "

        if self.is_hadoop:
            access_args += " -file " + models_name
            access_args += " -param models_filename='%s' " % \
                    self.output_name
        else:
            access_args += " -param models_filename='%s' " % \
                    os.path.join(self.output_path, self.output_name)

        self.mapreduce_routine(exe_program=self.exe_test,
                    input_file=os.path.join(self.data_path, self.sample_name),
                    output_file=os.path.join(self.output_path, self.output_test),
                    access_args=access_args,
                    content="Varify EL-SVL MapReduce Process")

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
    p = Parse()
    (options, args) = p.run()
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

