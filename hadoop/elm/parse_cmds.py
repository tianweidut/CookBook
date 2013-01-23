# -*- coding: UTF-8 -*-
'''
Created on 2012-12-24

@author: tianwei
'''
import sys

from optparse import OptionParser

__author__ = "tianwei"
__date__ = "December 24 2012"
__description__ = "command parser for main-wrapper"


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
        parse = OptionParser()
        parse.add_option("-o", "--openHadoop", action="store_true", dest="is_hadoop", 
                        help="whether it is running on hadoop platform")
        parse.add_option("-c", "--closeHadoop", action="store_false", dest="is_hadoop", 
                        help="whether it is running on hadoop platform")
        parse.add_option("-n", "--num", action="store", dest="num", 
                        help="num for elsvm")
        parse.add_option("-s", "--sampleName", action="store", dest="sample_name",
                        default="elsvm_data.csv", help="sample for elsvm")
        parse.add_option("-p", "--path", action="store", dest="path",
                        help="sample data path")
        parse.add_option("-t", "--output_path", action="store", dest="output_path",
                        help="result output path")
        parse.add_option("-l", "--local_path", action="store", dest="local_path",
                        help="local output path")
        parse.add_option("-m", "--output_name", action="store",
                        dest="output_name",
                        help="output name")
        parse.add_option("-d", "--dim", action="store", dest="dim",
                        help="dim number for sample data")
        parse.add_option("-i", "--enableIncrement", action="store_true", dest="is_increment",
                        help="use increment mode")
        parse.add_option("-z", "--disableIncrement", action="store_false", dest="is_increment",
                        help="disable increment mode")

        (options, args) = parse.parse_args()

        if len(sys.argv) < 2:
            print "Usages:"
            print "-o --openHadoop Open Hadoop Platform"
            print "-c --closeHadoop use dumbo local environment"
            print "-p --dataPath source sample data path"
            print "-n --num for el-svm "
            print "-d --dim for sample data "
            print "-s --sampleName sample Name "
            print "current args version is not completed, please get more\
            information fro code, sorry for that!"
            print "please enjoy! From tianwei *_* "
            return (None, None)

        return (options, args)
