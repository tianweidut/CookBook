# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import os
import random

from parse_cmds import Parse
from utility_mapreduce import mapreduce_routine, cat_routine
from w_matrix import generate_w_matrix

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "main-wrapper for elsvm"

SEP = ','   # Parse from file
HADOOP_PATH = os.environ["HADOOP_HOME"]


class ElsvmWrapper():
    """
    """
    exe_dir = os.path.abspath(os.path.dirname(__file__))
    exe_elsvm = os.path.join(exe_dir, "elsvm.py")
    exe_test = os.path.join(exe_dir, "testsvm.py") 

    output_test = "output_test.csv"

    def __init__(self, is_hadoop, data_path, output_path, local_path=None,
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
        self.local_path = local_path
        self.w_matrix_filename = os.path.join(self.local_path, "w_matrix_file")

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

        mapreduce_routine(is_hadoop=self.is_hadoop, exe_program=self.exe_elsvm,
                    input_file=os.path.join(self.data_path, self.sample_name),
                    output_file=os.path.join(self.output_path, self.output_name),
                    access_args=access_args,
                    content="EL-SVM MapReduce Process")
        
        # STEP2: dump output 
        self.model_args = os.path.join(self.local_path, self.output_name)
        if self.is_hadoop:
            cat_routine(
                    input_file=os.path.join(self.output_path, self.output_name), 
                    output_file=self.model_args)

        return self.model_args

    def test(self, models_name):
        """
        """
        # STEP1: dumbo main start
        access_args = " -param models_filename='%s' " % \
            os.path.join(self.local_path, self.output_name)
        access_args += " -overwrite yes "

        if self.is_hadoop:
            access_args += " -file " + models_name
            access_args += " -param models_filename='%s' " % \
                    self.output_name
        else:
            access_args += " -param models_filename='%s' " % \
                    os.path.join(self.output_path, self.output_name)

        mapreduce_routine(is_hadoop=self.is_hadoop, exe_program=self.exe_test,
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
            local_path=options.local_path,
            sample_name=options.sample_name)
    e.run() 

