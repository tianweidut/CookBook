# -*- coding: UTF-8 -*-
'''
Created on 2012-11-20

@author: tianwei
'''
# Json Test

import simplejson
import os,sys

class SerializerRegistery(object):
    def __init__(self):
        self._classes = {}
    def add(self,cls):
        self._classes[cls.__module__,cls.__name__] = cls
        return cls
    def object_hook(self,dct):
        module,cls_name = dct.pop('__type__',(None,None))
        if cls_name is not None:
            return self._classes[module,cls_name].from_dict(dct)
        else:
            return dct
    def default(self,obj):
        dct = obj.to_dict()
        dct['__type__'] = [type(obj).__module__,
                           type(obj).__name__]
        return dct

registry = SerializerRegistery()

class A(object):
    time = None
    str = None
    list = None
    externObject = None
   
@registry.add    
class B(object):
    b1 = None
    b2 = None
    
        
    def __init__(self):
        pass
    
    def __repr__(self):
        return str(self.__dict__)
    def to_dict(self):
        return dict(self.__dict__)
    
    @classmethod
    def from_dict(cls,dct):
        return cls(**dct)  

@registry.add 
class C(object):
    c1 = None
    
        
    def __init__(self):
        pass
    
    def __repr__(self):
        return str(self.__dict__)
    def to_dict(self):
        return dict(self.__dict__)
    
    @classmethod
    def from_dict(cls,dct):
        return cls(**dct)  

@registry.add
class Test(object):
    time = None
    str = None
    list = None
    externObject = None
    
    def __init__(self):
        pass
    
    def __repr__(self):
        return str(self.__dict__)
    def to_dict(self):
        return dict(self.__dict__)
    
    @classmethod
    def from_dict(cls,dct):
        return cls(**dct)    

def main():
    a = A()
   
    a.time = "test"
    a.str = "str"
    a.list = []
    a.list.append("list-1")
    a.list.append("list-2")
    a.externObject = B()
    a.externObject.b1 = "b1"
    a.externObject.b2 = C()
    a.externObject.b2.c1 = "C1"

    result = simplejson.dumps(a, default=lambda o: o.__dict__)
    
    print result
    obj = simplejson.loads(result,strict=False)
    
    a = Test()
    a.time = "test"
    a.str = "str"
    a.list = []
    a.list.append("list-1")
    a.list.append("list-2")
    a.externObject = B()
    a.externObject.b1 = "b1"
    #a.externObject.b2 = C()
    #a.externObject.b2.c1 = "C1"
    
    print a.__getattribute__('time')
    a.__setattr__('time','fixed')
    print a.time
    print a.__getattribute__('time')
    
    #s = simplejson.dumps(a,default=registry.default)
    #print s
    #r = simplejson.loads(s,object_hook=registry.object_hook)
    #print r
    c = {'1':'test1','2':'test2','3':'test3'}
    a = ('1','2','3')
    for item in a:
        print type(item)
        print c[item]

if __name__ == "__main__":
    main()

    
