# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

Updated on 2013-01-21

@author: tianwei
'''
import os

from parse_cmds import Parse
from utility_mapreduce import mapreduce_routine, cat_routine
from w_matrix import generate_w_matrix
from models import generate_model

from config_acc import DATASETS, A_INC
from testsvm_generator_model import testsvm_generator

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "main-wrapper for eelsvm"


class ElsvmWrapper():
    """
    """
    exe_dir = os.path.abspath(os.path.dirname(__file__))
    exe_elsvm = os.path.join(exe_dir, "elsvm.py")
    exe_test = os.path.join(exe_dir, "testsvm_step3.py")

    exe_eelsvm = os.path.join(exe_dir, "eelsvm.py")
    exe_testsvm1 = os.path.join(exe_dir, "testsvm_step1.py")
    exe_testsvm2 = os.path.join(exe_dir, "testsvm_step2.py")

    output_test = "output_test.csv"

    def __init__(self, is_hadoop, data_path, output_path, local_path=None,
                 n=100, dim=2, v=100,
                 is_increment=False,
                 sample_name=None,
                 h_argument=20,
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
        self.final_result_filename = os.path.join(self.local_path, "final_result")
        self.is_increment = is_increment
        self.h_argument = h_argument
        if self.is_increment:
            self.result_inc_init()

    def result_inc_init(self):
        """
        incremented model file init
        """
        self.final_result_filename_inc = os.path.join(self.local_path, "final_result_inc")
        self.final_result_filename_inc_f = open(self.final_result_filename_inc, "w")
        self.inc_model_str = ""

    def result_close(self):
        """
        output result incremented model
        """
        if self.is_increment:
            print self.inc_model_str
            self.final_result_filename_inc_f.close()

    def mapreduce(self, sample_name, output_name, is_increment=False):
        """
        the whole routine of training mapreduce
        """
        # step1: elsvm mapreduce
        print "*" * 40
        print "step1: elsvm mapreduce"
        output_name_step1 = sample_name + "_step1"
        result_name = self.elsvm_mapreduce(sample_name=sample_name,
                                           output_name=output_name_step1)

        print "^" * 40
        # step2: generate model data file
        print "*" * 40
        print "step2: generate model data file"
        model_name = generate_model(input_filename=result_name,
                                    output_filename=result_name + "2",
                                    w_matrix_filename=self.w_matrix_filename,
                                    num=self.num,
                                    v=self.v,
                                    is_increment=is_increment,
                                    a_inc=float(A_INC))

        print "^" * 40
        # step3: testsvm_step1.py for cnt and means
        print "step3: testsvm_step1.py for cnt and means"
        print "*" * 40
        output_testsvm_step1 = sample_name + "_testsvm_step1"
        result_argument = self.testsvm_step1(models_name=model_name,
                                             sample_name=sample_name,
                                             output_name=output_testsvm_step1)

        print "^" * 40
        # step4: testsvm_step2.py for another dataset
        print "step4: testsvm_step2.py for another dataset"
        print "*" * 40
        output_testsvm_step2 = sample_name + "_testsvm_step2"
        self.testsvm_step2(models_name=model_name,
                           sample_name=sample_name,
                           output_name=output_testsvm_step2)

        print "^" * 40
        # step5: eelsvm mapreduce
        print "step5: eelsvm mapreduce"
        print "*" * 40
        output_name_final = sample_name + "_final_step"
        result_final = self.eelsvm_mapreduce(sample_name=output_testsvm_step2,
                                             output_name=output_name_final,
                                             models_name=result_argument)

        return result_final
        print "^" * 40

    def elsvm_mapreduce(self, sample_name, output_name):
        """
        use elsvm.py to generate the basic globalH and globalD,
        for generating model
        """
        # add args for elsvm mapreduce
        args = self.get_basic_args()
        args += self.get_w_matrix_args()

        model_args = self.mapreduce_core(sample_name=sample_name,
                                         output_name=output_name,
                                         exe_file=self.exe_elsvm,
                                         is_cat=True,
                                         args=args)

        return model_args

    def testsvm_step1(self, models_name, sample_name, output_name):
        """
        use testsvm_step1.py to generate count and means,
        for eelsvm, need to cat to local file
        """
        args = self.get_file_args(models_name)

        h_args = self.mapreduce_core(sample_name=sample_name,
                                     output_name=output_name,
                                     exe_file=self.exe_testsvm1,
                                     is_cat=True,
                                     args=args)
        return h_args

    def get_file_args(self, models_name):
        """"""
        access_args = " -overwrite yes "

        if self.is_hadoop:
            access_args += " -file " + models_name

        access_args += " -param models_filename='%s' " % \
                       os.path.basename(models_name)

        return access_args

    def get_basic_args(self):
        """"""
        access_args = " -param v='%s' " % (self.v)
        access_args += " -param num='%s' " % (self.num)

        return access_args

    def testsvm_step2(self, models_name, sample_name, output_name):
        """
        use testsvm_step2.py to generate another dataset,
        for eelsvm, only in hadoop clusters
        """
        args = self.get_file_args(models_name)

        self.mapreduce_core(sample_name=sample_name,
                            output_name=output_name,
                            exe_file=self.exe_testsvm2,
                            is_cat=False,
                            args=args)

    def eelsvm_mapreduce(self, sample_name, output_name, models_name):
        """
        use eelsvm.py to generate final globalH and globalD,
        for testsvm_step3.py
        """
        args = self.get_w_matrix_args()

        # get models args
        h_trans, means = testsvm_generator(self.h_argument,
                                           os.path.join(self.local_path,
                                                        models_name))

        args += " -param h_trans='%s' " % (str(h_trans))
        args += " -param means='%s' " % (str(means))

        model_args = self.mapreduce_core(sample_name=sample_name,
                                         output_name=output_name,
                                         exe_file=self.exe_eelsvm,
                                         is_cat=True,
                                         args=args)

        return model_args

    def get_w_matrix_args(self):
        """
        Add w_matrix args
        """

        if self.is_hadoop:
            access_args = " -file " + self.w_matrix_filename
            access_args += " -param w_matrix_filename='%s' " % \
                (os.path.basename(self.w_matrix_filename))
        else:
            access_args = " -param w_matrix_filename='%s' " % \
                (self.w_matrix_filename)

        return access_args

    def mapreduce_core(self, sample_name, output_name,
                       exe_file=None,
                       is_cat=True,
                       args=None):
        """
        core mapreduce in hadoop
        """
        # STEP1: dumbo main start
        mapreduce_routine(is_hadoop=self.is_hadoop, exe_program=exe_file,
                          input_file=os.path.join(self.data_path, sample_name),
                          output_file=os.path.join(self.output_path, output_name),
                          access_args=args,
                          content="EL-SVM MapReduce Process")

        # STEP2: dump output
        if not is_cat:
            return

        self.model_args = os.path.join(self.local_path, output_name)
        if self.is_hadoop:
            cat_routine(input_file=os.path.join(self.output_path,
                                                output_name),
                        output_file=self.model_args)

        return self.model_args

    def test(self, models_name, input_name, output_name):
        """
        """
        # STEP1: dumbo main start
        access_args = self.get_file_args(models_name)

        mapreduce_routine(is_hadoop=self.is_hadoop,
                          exe_program=self.exe_test,
                          input_file=os.path.join(self.data_path,
                                                  input_name),
                          output_file=os.path.join(self.output_path,
                                                   output_name),
                          access_args=access_args,
                          content="Varify EL-SVL MapReduce Process")

        # STEP2: dump the result
        if self.is_hadoop:
            cat_routine(input_file=os.path.join(self.output_path,
                                                output_name),
                        output_file=self.final_result_filename)
        # STEP3: output result
        self.show_result()

    def show_result(self):
        """
        """
        f = open(self.final_result_filename, "r")
        contents = f.readlines()

        tmp = "\n" + "*" * 20 + "\n"

        # Parse multi-lines
        true_cnt = int(contents[0].split("\t")[1])
        false_cnt = int(contents[1].split("\t")[1])

        tmp += "true:%d, false:%d \n" % (true_cnt, false_cnt)
        total_num = true_cnt + false_cnt
        if total_num > 10000:
            tmp += "total nums:%d w \n" % (total_num / 10000)
        elif total_num > 1000:
            tmp += "total nums:%d k \n" % (total_num / 1000)
        else:
            tmp += "total nums:%d \n" % (total_num)

        tmp += "accuracy rate: %f%% \n" % (true_cnt / float(total_num) * 100.0)

        tmp += "\n" + "*" * 20 + "\n"

        # output result
        print tmp
        if self.is_increment:
            self.inc_model_str += tmp
            print >> self.final_result_filename_inc_f, tmp

        f.close()

    def run(self):
        """
        """
        # STEP1: generate random matrix w
        generate_w_matrix(filename=self.w_matrix_filename,
                          dim=self.dim,
                          num=self.num)

        # STEP2: mode choice
        if self.is_increment:
            self.run_increment_mode()
        else:
            self.run_single_mode()

        # STEP 3: (optional) close inc model mode
        self.result_close()

    def run_increment_mode(self):
        """
        increment modle
        """
        model_name = None
        for cnt, sample_name in enumerate(DATASETS):
            # STEP1: accuracy result
            if cnt != 0:
                self.test(models_name=model_name,
                          input_name=sample_name,
                          output_name=self.output_test)

            # STEP2: call mapreduce, generate raw H and D
            output_name = sample_name + "out"
            result_name = self.mapreduce(sample_name=sample_name,
                                         output_name=output_name,
                                         is_increment=True)

            # STEP3: generate incremented model
            model_name = generate_model(input_filename=result_name,
                                        output_filename=result_name + "2",
                                        w_matrix_filename=self.w_matrix_filename,
                                        num=self.num,
                                        v=self.v,
                                        is_increment=True,
                                        a_inc=float(A_INC))

    def run_single_mode(self):
        """
        traditional single mode
        """
        # STEP1: map-reduce
        result_name = self.mapreduce(sample_name=self.sample_name,
                                     output_name=self.output_name)

        # STEP2: generate model
        result_name2 = generate_model(input_filename=result_name,
                                      output_filename=result_name + "2",
                                      w_matrix_filename=self.w_matrix_filename,
                                      num=self.num,
                                      v=self.v)

        # STEP3: test for mapreduce
        self.test(models_name=result_name2,
                  input_name=self.sample_name,
                  output_name=self.output_test)


if __name__ == "__main__":
    p = Parse()
    (options, args) = p.run()
    e = ElsvmWrapper(is_hadoop=options.is_hadoop,
                     data_path=options.path,
                     n=options.num,
                     v=options.var,
                     dim=options.dim,
                     output_name=options.output_name,
                     output_path=options.output_path,
                     local_path=options.local_path,
                     sample_name=options.sample_name,
                     is_increment=options.is_increment,
                     h_argument=options.h_argument)

    e.run()
