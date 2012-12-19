# -*- coding: UTF-8 -*-
'''
Created on 2012-11-5

@author: tianwei

Theme: some tricks on closure function, we will write a Decorators for log
'''

import time 
import sys

"""We can use this fuc as a Decorator function to record the time of function"""
def log():
    def show_args(f,*args,**kargs):
        print """
            function name   : %s
            params          : %r
            ket params      : %r
            other...        : %s
        """ %(f.__name__,args,kargs,'###'*10)

    def logfuncs(f):
        def closure_log(*args,**kargs):
            now = time.time()
            try:
                """It will call core function"""
                return f(*args,**kargs)
            finally:
                """Use closure feature """
                show_args(f,*args,**kargs)
                print "Call timedelta: %s "%(time.time()-now)
        return closure_log
    try:
        return logfuncs
    except KeyError,e:
        raise ValueError(e),'None'

"""Example"""
@log()
def fibonacii_lambda(n):
    return map(lambda x,f=lambda x,f:f(x-1,f)+f(x-2,f) if x>1 else 1:f(x,f)
            ,xrange(0,n))

@log()
def fibonacii_recursion(n):
    def closure_fib_recursion(p):
        return int(1 if p in [0,1] else closure_fib_recursion(p-1) + closure_fib_recursion(p-2))
    return [closure_fib_recursion(x) for x in xrange(0,n)]

@log()
def primes_list(n):
    return [x for x in xrange(0,n) if not [y for y in xrange(2,int(x ** 0.5 +1)) if x % y == 0 ]]

def test():
    print fibonacii_lambda(30)
    print fibonacii_recursion(30)
    print primes_list(100)

if __name__ == "__main__":
    test()
