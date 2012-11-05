# -*- coding: UTF-8 -*-
'''
Created on 2012-11-5

@author: tianwei
'''
#Decorators for Functions and Methods
#Resource: http://www.python.org/dev/peps/pep-0318/

from time import ctime, sleep

def runFunc(func):
    def wrappedFunc():
        print '[%s] %s() called' %(ctime(),func)
        return func()
    #print 'runFunc called!'
    #print 'wrapped Func %s'%wrappedFunc
    return wrappedFunc

@runFunc
def replaceFunc():
    print "in replace Func"
    pass

if __name__ == "__main__":
    print "start!"
    print "replace func: %s"%replaceFunc
    replaceFunc()

