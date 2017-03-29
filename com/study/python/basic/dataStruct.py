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
    ‘filter(function, sequence)' returns a sequence consisting of those items from the sequence for which func- tion(item) is true.
    If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list
'''
def f(x): return x % 2 != 0 and x % 3 != 0
print filter(f, range(2, 25))
print '-'*100

'''
    Functional Programming Tools: map()
    ‘map(function, sequence)' calls function(item) for each of the sequence's items and returns a list of the return values
'''
def cube(x): return x * x * x
print map(cube, range(1, 11))
seq = range(8)
def add(x,y): return x+y
print map(add, seq, seq)
print '-'*100

'''
    Functional Programming Tools: reduce()
    ‘reduce(function, sequence)' returns a single value constructed by calling the binary function function on the first two items of the sequence,
    then on the result and the next item, and so on
'''
def add(x,y): return x+y
print reduce(add, range(1, 11))
print '-'*100

def sumFunc(seq):
    def add(x,y): return x+y
    return reduce(add, seq, 'acb')
print sum(range(1, 11))
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
print '-'*100

'''
    Dictionary structure
    It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary)
'''
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['sape']
del tel['guido']
print tel
print tel.keys()
print tel.has_key('jack')
print tel.values()
tel.pop('jack')
print tel
print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print dict(sape=4139, guido=4127, jack=4098)
print '-'*100

# Loop techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v
print '-'*100

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions,answers):
    print 'What is your %s? It is %s.' % (q, a)

for i in reversed(xrange(1, 10, 3)):
    print i

for f in sorted(set(basket)):
    print f
print '-'*100

str1, str2, str3 = '', 'abc', '123'
notNull = str1 or str2 or str3
print notNull
print '-'*100

'''
    Compare sequences and other types
    Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering:
        ﬁrst the ﬁrst two items are compared, and if they differ this determines the outcome of the comparison;
            if they are equal, the next two items are compared,
            and so on, until either sequence is exhausted.
    If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively.
    If all items of two sequences compare equal, the sequences are considered equal.
    If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one.
    Lexicographical ordering for strings uses the ASCII ordering for individual characters. Some examples of comparisons between sequences of the same type
'''
print (1, 2, 3) < (1, 2, 4) 
print [1, 2, 3] < [1, 2, 4] 
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4) < (1, 2, 4)
print (1, 2) < (1, 2, -1)
print (1, 2, 3) == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
print '-'*100