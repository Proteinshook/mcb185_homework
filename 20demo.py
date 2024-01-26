# 20demo.py by Ethan Djou

import math
print('hello, again')        # greeting

"""
this is
a
multi-line comment
"""

print(1.2e-3)                # able to print scientific notation

import math
print(int(math.sqrt(9)))
print(math.log(1))

a = 9                        # one side
b = 7                        # the other side
c = math.sqrt(a**2 + b**2)   # the hypotenuse
print(c)

print(type(a), type(b), type(c), sep=', ')


def greeting():              # the name must be followed by ():
	print('hello Ethan')

greeting() 

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

x = pythagoras(3, 4)
print(x)


def pythagoras2(a, b):      # It is not required to have variable c or x
	assert(a > 0)
	assert(b > 0)
	return math.sqrt(a**2 + b**2)

print(pythagoras2(3, 4))
print(pythagoras2(13, 14))

"""
Write a function that turns negative numbers into positive numbers and vise versa.
Give your function a name that is simultaneously simple and descriptive.
"""
def reversecharge(a):
	if a > 0: return a * -1
	if a < 0: return abs(a)
	if a == 0: return 'please use a number other than zero.'

print(reversecharge(0))

# Write functions that compute the area, circumference, or volumes of simple shapes like squares, rectangles, circles, spheres, etc.
def area(h, w):
	return h * w

print(area(2, 2))

def circum(r):
	return 2 * math.pi * r

print(circum(10))

def volume(x):
	return (4 / 3) * math.pi * math.pow(x, 3)

print(volume(3))

s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')
print(a, b)

c = 2 == 3
print(c)
print(type(c))

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')
	
print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')


