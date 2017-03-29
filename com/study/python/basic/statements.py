#!/user/bin/python
# -*- coding: UTF-8 -*-




# slice notation
arr = ['cat','chicken','duck','elephant']
for x in arr[:]:
    if len(x) > 3:
        arr.append(x)
print arr

# range statement
print range(10)
print range(5,10)
print range(-10,-100,-10)
for i in range(len(arr)):
    print i , arr[i]

# break statement
for n in range(0,10):
    for x in range(2,n):
        if n % x ==0:
            print n, 'equals', x, '*', n/x
            break
        else:
            print n, 'is a prime number'


# pass statement
while True:
    pass
    break



# define function
def fib(n):
    ''' Print a Fibonacci series up to n.'''
    strVal = ''
    a, b = 0, 1
    while b < n:
        strVal = strVal + ' ' + str(b)
        a, b = b, a+b
    print strVal
fib(10)

def fib2(n):
    ''' Return a list containing the Fibonacci series up to n.'''
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
print fib2(10)

# default func args
i = 5
def f(arg=i):
    print arg
i = 6
f()
print '-'*100

'''
    The default func value is evaluated only once
    Notice : default value will be shared between subsequent calls .
'''
def f(a,L=[]):
    L.append(a)
    return L
print f(1)
print f(2)
print f(3)
print '-'*100

'''
    default value will not be shared between subsequent calls
'''
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print f2(1)
print f2(2)
print f2(3)
print f2(4,['aaa'])
print f2(5,L=['bbb'])
print '-'*100

'''
    Keyword Arguments
'''
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn’t", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It’s", state, "!"
parrot(action = 'VOOOOOM', voltage = 1000000)
parrot('a thousand', state = 'pushing up the daisies')
parrot('a million', 'bereft of life', 'jump')
print '-'*100

'''
    Keyword Arguments : dictionary func args
'''
def cheeseshop(kind, *args , **keywords):
    print "-- Do you have any", kind, '?'
    print "-- I'm sorry , we're all out of", kind
    for arg in args: print arg
    print '-'*40
    keys = keywords.keys()
    keys.sort()
    for kw in keys: print kw, ':', keywords[kw]
cheeseshop('Humburger', "It's very runny,sir.", "It's really very, VERY runny,sir.", client='John Cleese', shopkeeper='Michael Palin', aketch='Cheese Shop Sketch')
print '-'*100


'''
    Unpacking Argument Lists
'''
args = [3,6]
print range(*args)
d = {"voltage": "four million", "state": "bleedin’ demised", "action": "VOOM"}
parrot(**d)
print '-'*100


'''
    lambda expression
'''
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print f
print f(0)
print f(1)


'''
    Documentation Strings
'''
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print my_function.__doc__