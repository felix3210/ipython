#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 13:46
# @Author  : felix
# @Contact : wi1024u@gmail.com
# @File    : modules.py
# @Desc    : Modules模块管理


'''
    repr() str()
    The str() function is meant to return representations of values which are fairly human-readable,
    while repr() is meant to generate representations which can be read by the interpreter
'''
s = 'hello'
print str(s)
print repr(s)
print str(0.1)
print repr(0.1)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '....'
print s

hello = 'hello, world\n'
print repr(hello)
print repr((x, y , ('spam', 'eggs')))
print '-'*100


for x in range(1,11):
    print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)
#
# for x in range(1, 11):
#     print '%2d %3d %4d' % (x, x*x, x*x*x)
print '-'*100
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: %(Jack)d; Sjoerd: %(Sjoerd)d; Dcab: %(Dcab)d' % table
print '%d\n' % 10 , '%2d\n' % 11, '%3d' % 12
