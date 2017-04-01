#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 17:21
# @Author  : felix
# @Contact : wi1024u@gmail.com
# @File    : exceptions.py
# @Desc    : Introduce python exceptions & how to handle exception

import sys

# while True:
#     try:
#         x = int(raw_input("Please enter a number: "))
#         break
#     except ValueError, detail:
#         print "Oops! That was no valid number . Try again ... %s " % detail
#     except:
#         print "Unexpected error:", sys.exc_info()
# print '-'*100

# try:
#     f = open('/tmp/q.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError, (errno, strerror):
#     print "I/O error(%s): %s" %(errno, strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# except:
#     print "Unexpected error:", sys.exc_info()[0]
#     raise
# else:
#     print 'file has', len(f.readlines()) , 'lines'
#     f.close()
# print '-'*100
#
#
# try:
#     raise Exception('spam', 'eggs')
# except Exception, inst:
#     print type(inst)
#     print inst.args
#     print inst
#     x, y = inst
#     print 'x =', x, '\n', 'y =', y
# print '-'*100


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError('custom except')
except MyError, e:
    print 'My exception occurred , value :', e.value
print '-'*100

with open('/tmp/q.txt') as f:
    for line in f:
        print line

print '-'*100

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print 'division by zero!'
    else:
        print 'result is', result
    finally:
        print 'executing finally clause'
divide(2, 1)
divide(2, 0)
divide("2", "1")
print '-'*100