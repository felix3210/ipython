#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/28 16:16
# @Author  : felix
# @Contact : wi1024u@gmail.com
# @File    : dataStruct.py
# @Desc    : Data Structures


'''
    List
'''
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
a.insert(2, -1)
a.append(333)
print a
print a.index(333)
a.remove(333)
print a
a.reverse()
print a
a.sort()
print a
print '-'*100

'''
    Using Lists as Stacks
'''
print a.pop()
print a.pop()
print a
print '-'*100

'''
    Using Lists as Queues
'''
print a.pop(0)
print a.pop(0)
print a
print '-'*100

'''
    Functional Programming Tools: filter()
    ‘filter(function, sequence)’ returns a sequence consisting of those items from the sequence for which func- tion(item) is true.
    If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list
'''
def f(x): return x % 2 != 0 and x % 3 != 0
print filter(f, range(2, 25))
print '-'*100

'''
    Functional Programming Tools: map()
    ‘map(function, sequence)’ calls function(item) for each of the sequence’s items and returns a list of the return values
'''
def cube(x): return x * x * x
print map(cube, range(1, 11))
seq = range(8)
def add(x,y): return x+y
print map(add, seq, seq)
print '-'*100

'''
    Functional Programming Tools: reduce()
    ‘reduce(function, sequence)’ returns a single value constructed by calling the binary function function on the first two items of the sequence,
    then on the result and the next item, and so on
'''
def add(x,y): return x+y
print reduce(add, range(1, 11))
print '-'*100

def sumFunc(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 'acb')
print sum(range(1,11))
print sum([])
print '-'*100

'''
    List Comprehensions
    List comprehensions provide a concise way to create lists without resorting to use of map(), ﬁlter() and/or lambda. The resulting list deﬁnition tends often to be clearer than lists built using those constructs.
    Each list comprehension consists of an expression followed by a for clause, then zero or more for or if clauses. The result will be a list resulting from evaluating the expression in the context of the for and if clauses which follow it.
    If the expression would evaluate to a tuple, it must be parenthesized
'''
freshfruit = [' banana', 'loganberry ', ' passion fruit ']
print [weapon.strip() for weapon in freshfruit]

vec = [2, 4, 6]
print [3*x for x in vec]
print [3*x for x in vec if x>3]
print [x*x for x in vec if x<3]
print [[x, x**2] for x in vec]
print [(x, x**2) for x in vec]

vec1 = [2, 4, 6]
vec2 = [4, 3, -9, 1, 10]
print [x*y for x in vec1 for y in vec2]
print [x+y for x in vec1 for y in vec2]
print [vec1[i]*vec2[i] for i in range(len(vec1))]
print [str(round(355/113.0, i)) for i in range(1,6)]
print '-'*100

'''
    del statement
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:]
print a
print '-'*100


'''
    Tuples structure
    A tuple consists of a number of values separated by commas
'''
t = 12345, 543, 'hello'
print t
print t[0]
u = t, (1, 2, 3, 4, 5)
print u
x, y, z = t
print x, '-', y, '-', z
print '-'*100

'''
    Sets structure
    A set is an unordered collection with no duplicate elements.
'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit
print 'orange' in fruit

a = set('abracadabra')
b = set('alacazam')
print a , b
print a - b
print a | b
print a & b
print a ^ b