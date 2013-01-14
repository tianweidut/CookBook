# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import os

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "main-wrapper for elsvm"

HADOOP_PATH = os.environ["HADOOP_HOME"]


def mapreduce_routine(is_hadoop, exe_program, input_file, output_file,
                      access_args="",
                      content=""):
    """
    """
    args = " dumbo start " + exe_program
    if is_hadoop:
        args += " -hadoop " + HADOOP_PATH

    args += " -input " + input_file
    args += " -output " + output_file
    args += " -overwrite yes "
    args += access_args

    print args
    print "+++In map-reduce phase+++"
    ret = os.system(args)

    if ret != 0:
        raise ValueError("%s process error!" % (content))
    else:
        print "---------Finish the %s process --------" % (content)


def cat_routine(input_file, output_file):
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
