# -*- coding: UTF-8 -*-
'''
Created on 2012-12-19

@author: tianwei
'''
import sys

__author__ = "tianwei"
__date__ = "December 19  2012"
__description__ = "debug"


def debug(content, pos=None):
    print >> sys.stderr, "+" * 15
    if pos is not None:
        print >> sys.stderr, pos
    print >> sys.stderr, content
    print >> sys.stderr, "-" * 15
