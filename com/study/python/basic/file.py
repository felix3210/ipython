#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 16:56
# @Author  : felix
# @Contact : wi1024u@gmail.com
# @File    : file.py
# @Desc    : Reading and writing files

import pickle
f = open('/data/code/ipython/com/study/python/model/UserDTO.py')
print f.read(10)
print f.readline()
print f.readlines()
for line in f:
    print line,
print '-'*100
f.seek(5)
print f.read(1)
f.seek(-3, 1)
print f.read(1)
f.close()
print '-'*100

f2 = open('/tmp/q.txt', 'r+')
val = {'abc': 'hello', 'age': 100}
f2.write(str(val))
f2.close()
print '-'*100

f3 = open('/tmp/q.txt', 'r+')
val = {'abc': 'hello', 'age': 100}
pickle.dump(val, f3)
f3.close()
print '-'*100

f4 = open('/tmp/q.txt')
val = pickle.load(f4)
print val
f4.close()
print '-'*100
