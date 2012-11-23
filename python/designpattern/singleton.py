#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Singleton for Python

###################
#Method A: metaclass

class Singleton(type):
    _instances = {}
    def __call__(cls,*args,**kwargs):
        if cls is not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class TestClass(BaseClass):
    __metaclass__ = Singleton
    

