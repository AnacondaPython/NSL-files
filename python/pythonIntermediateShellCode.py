Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str = 'Merlin'
>>> numbers = [1,2,3]
>>> tee = tuple('applpe', 'orange', 'banana)
	    
SyntaxError: EOL while scanning string literal
>>> tee = ('apple', 'orange', 'banana'
       str
       
SyntaxError: invalid syntax
>>> str
'Merlin'
>>> numbers
[1, 2, 3]
>>> tee

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tee
NameError: name 'tee' is not defined
>>> tee = ('apple', 'orange', 'banana')
>>> tee
('apple', 'orange', 'banana')
>>> i.next()

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    i.next()
NameError: name 'i' is not defined
>>> i.next()

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    i.next()
NameError: name 'i' is not defined
>>> i =iter (str)
>>> i.next()
'M'
>>> i.next()
'e'
>>> i.next()
'r'
>>> 
>>> i.next()
'l'
>>> i.next()
'i'
>>> i.next()
'n'
>>> def infinity ():
	count = 0
	yield count
	while True:
		count +=1
		yield count

		
>>> def bad_infinity ():
	count = 0
	return count
bad_infinity ()
SyntaxError: invalid syntax
>>> bad_infinity()

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    bad_infinity()
NameError: name 'bad_infinity' is not defined
>>> bad_infinity()

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    bad_infinity()
NameError: name 'bad_infinity' is not defined
>>> def bad_infinity():
	count = 0
	return count

>>> bad_infinity()
0
>>> bad_infinity()
0
>>> def bad _infinity():
	
SyntaxError: invalid syntax
>>> def bad_infinity():
	count = 0
	while True
	
SyntaxError: invalid syntax
>>> def bad_infinity():
	count=0
	while True
	
SyntaxError: invalid syntax
>>> def bad_infinity():
	count=0
	while True:
		count+=1
		return count

	
>>> inf=infinity()
>>> inf.next()
0
>>> inf.next()
1
>>> inf.next()
2
>>> inf.next()
3
>>> inf.next()
4
>>> inf.next()
5
>>> for i in inf:
	print i
	if i%3 ==0
	
SyntaxError: invalid syntax
>>> for i in inf:
	print i
	if i % 3 ==0:
		break

	
6
>>> inf.next()
7
>>> inf.next()

8
>>> inf.next()

9
>>> inf.next()

10
>>> inf.next()

11
>>> inf.next()

12
>>> inf.next()

13
>>> inf.next()

14
>>> inf.next()

15
>>> inf.next()

16
>>> range (10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range (3,10)
[3, 4, 5, 6, 7, 8, 9]
>>> range (3,10,3)
[3, 6, 9]
>>> range(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> for i in range 200
SyntaxError: invalid syntax
>>> for i in xrange(200):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
>>> a = xrange (10)
>>> print (a)
xrange(10)
>>> a.iter()

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.iter()
AttributeError: 'xrange' object has no attribute 'iter'
>>> a.iter():
	
SyntaxError: invalid syntax
>>> a.next

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.next
AttributeError: 'xrange' object has no attribute 'next'
>>> a.next))
SyntaxError: invalid syntax
>>> a.next()

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.next()
AttributeError: 'xrange' object has no attribute 'next'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> xrange (10)
xrange(10)
>>> [1.2.3]
SyntaxError: invalid syntax
>>> [1,2,3]
[1, 2, 3]
>>> l = []
>>> l.append(1)
>>> l.append(2)
>>> l.append(3)
>>> True.__repr__()
'True'
>>> l = (1,2,3)
>>> l
(1, 2, 3)
>>> l.append(3)

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    l.append(3)
AttributeError: 'tuple' object has no attribute 'append'
>>> l = [1,2,3]
>>> l[1]
2
>>> d = {}
>>> d = {'key':'value'}
>>> d.keys()
['key']
>>> d.values()
['value']
>>> d['key']
'value'
>>> d
{'key': 'value'}
>>> d
{'key': 'value'}
>>> fp - open ('text.txt','w')

Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    fp - open ('text.txt','w')
NameError: name 'fp' is not defined
>>> fp = open('test.txt','w')
>>> fp
<open file 'test.txt', mode 'w' at 0x0000000002B0F6F0>
>>> fp.write("some value")
>>> fp.close()
>>> with open('test.txt', 'w') as fp:
	fp.write('another value ya')

	
>>> sum
<built-in function sum>
>>> tyoe(sum)

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    tyoe(sum)
NameError: name 'tyoe' is not defined
d
>>> dir(sum)
['__call__', '__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> __class__

Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    __class__
NameError: name '__class__' is not defined
>>> L_class_

Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    L_class_
NameError: name 'L_class_' is not defined
>>> _class_

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    _class_
NameError: name '_class_' is not defined
>>> ___class___

Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    ___class___
NameError: name '___class___' is not defined
>>> sum..__class__
SyntaxError: invalid syntax
>>> some.__class__

Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    some.__class__
NameError: name 'some' is not defined
>>> sum.__class__
<type 'builtin_function_or_method'>
>>> sum.__module__
'__builtin__'
>>> sum.__module__[3,2,1]

Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    sum.__module__[3,2,1]
TypeError: string indices must be integers, not tuple
>>> 1
1
>>> [3,2,1]
[3, 2, 1]
>>> [1,1,2,2,3,3]
[1, 1, 2, 2, 3, 3]
>>> set([1,1,2,2,3,3])
set([1, 2, 3])
>>> {1,1,2,2,3,3,3}
set([1, 2, 3])
>>> appples = 10
>>> apples

Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    apples
NameError: name 'apples' is not defined
>>> type(sum)
<type 'builtin_function_or_method'>
>>> type(sum)
<type 'builtin_function_or_method'>
>>> type(apples)

Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    type(apples)
NameError: name 'apples' is not defined
>>> apples = 10
>>> apples
10
>>> type(apples)
<type 'int'>
>>> apples = 'red'
>>> type(apples)
<type 'str'>
>>> int == type(apples)
False
>>> 
>>> count, color, cost_per_pound = (10,'red',6.69)
>>> count
10
>>> color
'red'
>>> cost_per_pound
6.69
>>> name = 'Merlin Corey'
>>> name.split()
['Merlin', 'Corey']
>>> first, last =name.split()
>>> first
'Merlin'
>>> last
'Corey'
>>> split_names = name.split()
>>> first = split_names [0]
>>> last = split_names[1]
>>> first, space, last=namepartition(' ')

Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    first, space, last=namepartition(' ')
NameError: name 'namepartition' is not defined
>>> first, space, last =name.partititon(' ')

Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    first, space, last =name.partititon(' ')
AttributeError: 'str' object has no attribute 'partititon'
>>> first
'Merlin'
>>> space

Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    space
NameError: name 'space' is not defined
>>> first, space, last = name.partition(' ')
>>> first
'Merlin'
s
>>> pace

Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    pace
NameError: name 'pace' is not defined
>>> space
' '
l
>>> ast

Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    ast
NameError: name 'ast' is not defined
>>> space
' '
>>> last
'Corey'
>>> 
>>> 
>>> 
>>> (57/100)
0
>>> 57 / 100.)
SyntaxError: invalid syntax
>>> (57 / 100.)
0.57
>>> (1337 / 21242.)*100
6.294134262310518
>>> 10 > 50
False
>>> 10 > 8
True
>>> 10 > 8
True
>>> 10 > 8 and 10 > 12
False
>>> 10 > 8 or 10 > 12
True
>>> True and False
False
>>> True and True
True
>>> if (x %2) ==0:
	print 'even'
else:
	print 'odd'

	

Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    if (x %2) ==0:
NameError: name 'x' is not defined
>>> x = 10
>>> 'even' if (x%2) ==0 else 'odd'
'even'
>>> 0 == false

Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    0 == false
NameError: name 'false' is not defined
>>> none == false

Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    none == false
NameError: name 'none' is not defined
>>> 10 == 1
False
>>> 1 == 1
True
>>> 1 ==1 and 0]
SyntaxError: invalid syntax
>>> 0 if 1 == 1 else 2
0
>>> 0 == false

Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    0 == false
NameError: name 'false' is not defined
>>> 1 == 1 and 0 or 2
2
>>> True and False or 2
2
>>> 0 if 1 == 1  else 2
0
>>> even_or_odd = lamda x: 'even' if x%2 ==0 else 'odd'
SyntaxError: invalid syntax
>>> even_or_odd = lambda x: 'even' if x%2 == 0 else 'odd'
>>> even_or_odd (23)
'odd'
>>> scores = (('Merlin', 123), ('Nz0', 256), ('DG', 1024))
>>> scores [0]
('Merlin', 123)
>>> scores_numbers = (123, 256, 1024)
>>> scores_numbers = list(scores_numbers)
>>> scores_numbers.sort(reverse=True)
[
>>> scores_numbers
[1024, 256, 123]
>>> list(sorted(scores_numbers))
[123, 256, 1024]
>>> scores
(('Merlin', 123), ('Nz0', 256), ('DG', 1024))
>>> list(sorted(scores, key=lambda x: x[1], reverse=True))
[('DG', 1024), ('Nz0', 256), ('Merlin', 123)]
>>> def x_of_one(x):
	return x[1]

>>> def identity(x):
	return x

>>> identity(10)
10
>>> identity(scores_numbers)
[1024, 256, 123]
>>> x_of_one(scores_numbers)
256
>>> age = 99
>>> if age <= 10:
	print "key"
elfi age > 10 and age <= 18:
	
SyntaxError: invalid syntax
>>> if age <=10:
	print 'under 10'
elseif age > 10 and age <= 18:
	
SyntaxError: invalid syntax
>>> if age <=10:
	print 'a'
elif age >10 and age <=18:
	print 'b'
	elif age >18 and <= 30:
		
SyntaxError: invalid syntax
>>> if age <= 10:
	print 'a'
elif age >10 and age <=18:
	print 'b'
elif age >18 and age <=30:
	print 'c'
else:
	print 'Age is number'

	
Age is number
>>> count - 19
-9
w
>>> counter = 10
>>> while counter >=0:
	 print 'Counting down...{}'.format(counter)
	 counter -=1

	 
Counting down...10
Counting down...9
Counting down...8
Counting down...7
Counting down...6
Counting down...5
Counting down...4
Counting down...3
Counting down...2
Counting down...1
Counting down...0
>>> Counting down...0
SyntaxError: invalid syntax
>>> 
>>> while counter >1:
	print 'Positive'
else:
	print 'egative'

	
egative
>>> l = range(10)
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l = iter(1)

Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    l = iter(1)
TypeError: 'int' object is not iterable
>>> l.next()

Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    l.next()
AttributeError: 'list' object has no attribute 'next'
>>> l = iter(l)
>>> l.next()
0
>>>  for i in l
 
  File "<pyshell#270>", line 2
    for i in l
    ^
IndentationError: unexpected indent
>>> for i in l:
	print 'Item: {}'.format(i)

	
Item: 1
Item: 2
Item: 3
Item: 4
Item: 5
Item: 6
Item: 7
Item: 8
Item: 9
>>> asdfasdf

Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    asdfasdf
NameError: name 'asdfasdf' is not defined
>>> 1 / 0

Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    1 / 0
ZeroDivisionError: integer division or modulo by zero
>>> divider = lambda x, y: x / (y - 1)
>>> divider (3,2)
3
>>> divider (3,1)

Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    divider (3,1)
  File "<pyshell#276>", line 1, in <lambda>
    divider = lambda x, y: x / (y - 1)
ZeroDivisionError: integer division or modulo by zero
>>> try:
	value = divider (3,1)
except ZeroDivisionError, e:
	print 'Slow Down there L\'Hopital'
	value = None

	
Slow Down there L'Hopital
>>> value
>>> None == value
True
>>> def test():
	print'Hello world'

	
>>> 
>>> test
<function test at 0x0000000002BC7208>
>>> test()
Hello world
>>> retval

Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    retval
NameError: name 'retval' is not defined
>>> retval = test()
Hello world
>>> retval
>>> None == retval
True
>>> def test ():
	print 'Hello World'
	return 0

>>> test()
Hello World
0
>>> Hello world
SyntaxError: invalid syntax
>>> test()
Hello World
0
>>> x - test()
Hello World
10
>>> x
10
>>> x = test()
Hello World
>>> x
0
>>> def add_ten(x)
SyntaxError: invalid syntax
>>> def add_ten(x):
	"""returns the number x plus 10, given x is a number"""
	return x + 10 if isinstance(x,int) else None

>>> add_ten(10)
20
>>> add_ten('Merlin')
>>> add_ten.__doc__
'returns the number x plus 10, given x is a number'
>>> help(add_ten)
Help on function add_ten in module __main__:

add_ten(x)
    returns the number x plus 10, given x is a number

help
>>> (sum)
<built-in function sum>
>>> str = 'Merlin'
>>> str = 'Merlin has paragraph. gggggggggggggggggggggggggggggg
SyntaxError: EOL while scanning string literal
>>> str = """Merlin has a pargaph
yyyyyyyyyyyyyyyyyyyy"""
>>> print str
Merlin has a pargaph


yyyyyyyyyyyyyyyyyyyy
>>> def add_two(first, seconds):
	return first+second

>>> add_two(1,10)

Traceback (most recent call last):
  File "<pyshell#329>", line 1, in <module>
    add_two(1,10)
  File "<pyshell#328>", line 2, in add_two
    return first+second
NameError: global name 'second' is not defined
>>> add_two(1,10)

Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    add_two(1,10)
  File "<pyshell#328>", line 2, in add_two
    return first+second
NameError: global name 'second' is not defined
>>> add_two('Merlin', 'NSL')

Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    add_two('Merlin', 'NSL')
  File "<pyshell#328>", line 2, in add_two
    return first+second
NameError: global name 'second' is not defined
>>> add_two(1,10)

Traceback (most recent call last):
  File "<pyshell#332>", line 1, in <module>
    add_two(1,10)
  File "<pyshell#328>", line 2, in add_two
    return first+second
NameError: global name 'second' is not defined
>>> def add_two (first, second):
	return first+second
add_two(1,10)
SyntaxError: invalid syntax
>>> add_two(1,10)

Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    add_two(1,10)
  File "<pyshell#328>", line 2, in add_two
    return first+second
NameError: global name 'second' is not defined
>>> def add_two (first, second):
	return first+second

>>> add_two(1,10)
11
>>> add_two('Merlin', 'NSL')
'MerlinNSL'
>>> add_two([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> add_two(1)

Traceback (most recent call last):
  File "<pyshell#344>", line 1, in <module>
    add_two(1)
TypeError: add_two() takes exactly 2 arguments (1 given)
>>> def print_args(*args):
	for arg in args:
		print 'Argument: {}'.format(arg)

		
>>> print_args
<function print_args at 0x0000000002C394A8>
>>> print_args()
>>> print_args(1,2,3)
Argument: 1
Argument: 2
Argument: 3
>>> def print_args(*args):
	print 'Argument:{}'.format(arg)

	
>>> add_two(1,2)
3
>>> add_two(first=1, second = 21)
22
>>> add_two(second=21, first=12)
33
>>> def mix(one, *args):
	mixed = 0
	for arg in args:
		mixed +=arg*one
		return mixed

	
>>> 
>>> mix(1)
>>> mix(1)
>>> def mix(one, *args):
	mixed = 0
	for arg in args:
		mixed +=arg*one
	return mixed

>>> mix(1)
0
>>> mix(1)
0
>>> mix(1,2,3)
5
>>> mix(1,2,3,4,5,6,7,8,9,10)
54
>>> l
<listiterator object at 0x0000000002BC25F8>
>>> l
<listiterator object at 0x0000000002BC25F8>
>>> l = range(10)
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> mix(*l)
0
>>> mixl = l [1:]
>>> mix(l)
0
>>> mix(l,1)

Traceback (most recent call last):
  File "<pyshell#382>", line 1, in <module>
    mix(l,1)
  File "<pyshell#370>", line 4, in mix
    mixed +=arg*one
TypeError: unsupported operand type(s) for +=: 'int' and 'list'
>>> mix(*l)== mix(1,2,3,4,5,6,7,8,9)
False
>>> def print_args(*args, **kwargs):
	for arg in args:
		print 'Argument:{}'.format(arg)
	for key in kwargs:
		print 'Key: {} Values:{}'.format(key, kwargs[key])

		
>>> print_args()
>>> print_args(1,2,3)
Argument:1
Argument:2
Argument:3
>>> print_args(1,2,3, name= 'Merlin', location = 'Nullspace', powerlevel = 9001)
Argument:1
Argument:2
Argument:3
Key: powerlevel Values:9001
Key: name Values:Merlin
Key: location Values:Nullspace
>>> dir
<built-in function dir>
>>> builtinfunctions

Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    builtinfunctions
NameError: name 'builtinfunctions' is not defined
>>> lvals = locals()
>>> first
'Merlin'
>>> lvals[;'
      
SyntaxError: invalid syntax
>>> lvals['Merlin']

Traceback (most recent call last):
  File "<pyshell#398>", line 1, in <module>
    lvals['Merlin']
KeyError: 'Merlin'
>>> lvals['Merlin']

Traceback (most recent call last):
  File "<pyshell#399>", line 1, in <module>
    lvals['Merlin']
KeyError: 'Merlin'
>>> lvals =[


	g

	g
	
SyntaxError: invalid syntax
>>> lvals['Merlin']

Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    lvals['Merlin']
KeyError: 'Merlin'
>>> first = 'Merlin'
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a', 'add_ten', 'add_two', 'age', 'apples', 'appples', 'bad_infinity', 'color', 'cost_per_pound', 'count', 'counter', 'd', 'divider', 'e', 'even_or_odd', 'first', 'fp', 'i', 'identity', 'inf', 'infinity', 'l', 'last', 'lvals', 'mix', 'mixl', 'name', 'numbers', 'print_args', 'retval', 'scores', 'scores_numbers', 'space', 'split_names', 'str', 'tee', 'test', 'value', 'x', 'x_of_one']
>>> dir(first)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(first)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> abs(-10)
10
>>> numbers = [1,3,5,9,10]
>>> oddp = lambda x: x %2 ==1
>>> oddp(1)
True
>>> all_odd = True
>>> for num in numbers:
	if not oddp (num):
		all_odd = False
		break

	
>>> all_odd
False
>>> all(oddp(num) for num in numbers)
False
>>> all([True,True,True,False])
False
>>> all([True,True])
True
>>> 
>>> bin(32)
'0b100000'
>>> bin(264)
'0b100001000'
>>> callable(first)
False
>>> callable(add_two)
True
>>> chr
<built-in function chr>
>>> ord
<built-in function ord>
>>> 'A'
'A'
>>> ord'A')
SyntaxError: invalid syntax
>>> chr(65)
'A'
>>> ord('A')
65
>>> chr(66)
'B'
>>> print 'ABCD' +char(8)

Traceback (most recent call last):
  File "<pyshell#438>", line 1, in <module>
    print 'ABCD' +char(8)
NameError: name 'char' is not defined
>>> print 'ABC' +chr(8)
ABC
>>> a
xrange(10)
>>> 
>>> complex (3+4)
(7+0j)
>>> d
{'key': 'value'}
>>> d['arbitrary'] = 1234
>>> d
{'key': 'value', 'arbitrary': 1234}
>>> d['arbitrary']
1234
>>> del d['arbitrary']
>>> delattr(d,'1234')

Traceback (most recent call last):
  File "<pyshell#449>", line 1, in <module>
    delattr(d,'1234')
AttributeError: 'dict' object has no attribute '1234'
>>> class Point (object):
	x = None
	y = None
	def __init__(self, x, y):
		self.x = x
		self.y = y

		
>>> p = Point (3,-3)
>>> p
<__main__.Point object at 0x0000000002BD8C18>
>>> p.x
3
p
>>> .y
SyntaxError: invalid syntax
>>> p.y
-3
>>> delattr(p,'x')
>>> p.x
>>> p.x = 3
>>> 
>>> 
>>> x, y = (1,2)
>>> enumerate(l)
<enumerate object at 0x0000000002BC46C0>
>>> list(enumerate(l))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i , name in enumerate(names):
	print '{} is #{}'.format(name, i)

	

Traceback (most recent call last):
  File "<pyshell#473>", line 1, in <module>
    for i , name in enumerate(names):
NameError: name 'names' is not defined
>>> names

Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    names
NameError: name 'names' is not defined
>>> names = ['Merlin', 'DG', 'BV']
>>> names
['Merlin', 'DG', 'BV']
>>> for i, name in enumerate(names)
SyntaxError: invalid syntax
>>> print

>>> print '{} is #{}'.format(name, i)
Merlin Corey is #9
>>> names [0]
'Merlin'
>>> for i in xrange(len(names)):
	print names (o)

	

Traceback (most recent call last):
  File "<pyshell#483>", line 2, in <module>
    print names (o)
NameError: name 'o' is not defined
>>> for i in xrange (len(names)):
	print names(i)

	

Traceback (most recent call last):
  File "<pyshell#486>", line 2, in <module>
    print names(i)
TypeError: 'list' object is not callable
>>> print eval ('"Hello" + name')
HelloMerlin Corey
>>> hex (255)
'0xff'
>>> hash (123)
123
>>> hash ([123, 456])

Traceback (most recent call last):
  File "<pyshell#490>", line 1, in <module>
    hash ([123, 456])
TypeError: unhashable type: 'list'
>>> name = raw_input('What is your name? ')
What is your name? gg
>>> isinstance (p,int)
False
>>> isinstance(p, Point)
True
>>> p
<__main__.Point object at 0x0000000002BD8C18>
>>> Point
<class '__main__.Point'>
>>> l = [1,2,3]
>>> max (l)
3
>>> pow(2,8)
256
>>> l.__repr__()
'[1, 2, 3]'
>>> list(reversed(l))
[3, 2, 1]
>>> l[0:2]
[1, 2]
>>> l[0:3]
[1, 2, 3]
>>> l[5:]
[]
>>> l[0:10:2]
[1, 3]
>>> l = range (10)
>>> l[0:10:2]
[0, 2, 4, 6, 8]
>>> slice(0,10,2)
slice(0, 10, 2)
>>> type(p)
<class '__main__.Point'>
>>> type('Point2',(),{'__init__':lambda self, x, y:

		  e

		  g
		  
SyntaxError: invalid syntax
>>> g

Traceback (most recent call last):
  File "<pyshell#516>", line 1, in <module>
    g
NameError: name 'g' is not defined
>>> def point_init(self,x,y):
	self.x=x
	self.y=y

	
>>> class Point:
	x = None
	y = None
	def __init__(self, x, y):
		self.x=x
		self.y=y

		
>>> Point2 = type('Point2',(), {'x':None, 'y':None, '__init__':point_init})
>>> hex(512)
'0x200'
>>> unichar(0x1F686)

Traceback (most recent call last):
  File "<pyshell#530>", line 1, in <module>
    unichar(0x1F686)
NameError: name 'unichar' is not defined
>>> unichr(0x1F686)

Traceback (most recent call last):
  File "<pyshell#531>", line 1, in <module>
    unichr(0x1F686)
ValueError: unichr() arg not in range(0x10000) (narrow Python build)
>>> unichr(0x1F686)

Traceback (most recent call last):
  File "<pyshell#532>", line 1, in <module>
    unichr(0x1F686)
ValueError: unichr() arg not in range(0x10000) (narrow Python build)
>>> unicode('Merlin')
u'Merlin'
>>> 'Merlin\x280'
'Merlin(0'
>>> vars(p)
{'y': -3, 'x': 3}
>>> p
<__main__.Point object at 0x0000000002BD8C18>
>>> Zip(names, scores_numbers)

Traceback (most recent call last):
  File "<pyshell#537>", line 1, in <module>
    Zip(names, scores_numbers)
NameError: name 'Zip' is not defined
>>> score_numbers

Traceback (most recent call last):
  File "<pyshell#538>", line 1, in <module>
    score_numbers
NameError: name 'score_numbers' is not defined
>>> score_numbers

Traceback (most recent call last):
  File "<pyshell#539>", line 1, in <module>
    score_numbers
NameError: name 'score_numbers' is not defined
>>> scores_numbers
[1024, 256, 123]
>>> zip(names, scores_numbers)
[('Merlin', 1024), ('DG', 256), ('BV', 123)]
>>> zip(names, scores_numbers, ('red', 'gree', 'blue', 'extra'))
[('Merlin', 1024, 'red'), ('DG', 256, 'gree'), ('BV', 123, 'blue')]
>>> map
<built-in function map>
>>> filter

Traceback (most recent call last):
  File "<pyshell#544>", line 1, in <module>
    ilter
NameError: name 'ilter' is not defined
>>> reduce
<built-in function reduce>
>>> \filter
SyntaxError: unexpected character after line continuation character
>>> filter
<built-in function filter>
>>> map
<built-in function map>
>>> filter
<built-in function filter>
>>> reduce
<built-in function reduce>
>>>  \\\m\\
 
  File "<pyshell#551>", line 2
    \\\m\\
    ^
IndentationError: unexpected indent
>>> map(add_ten, l)
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> new_list =[]
>>> for i in l:
	new_list.append(add_ten(i))

	
>>> new_list
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> new_list[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

Traceback (most recent call last):
  File "<pyshell#558>", line 1, in <module>
    new_list[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
TypeError: list indices must be integers, not tuple
>>> new_list
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> filter(oddp,l)
[1, 3, 5, 7, 9]
>>> oddp
<function <lambda> at 0x0000000002C54A58>
>>> new_list = []
>>> for i in l:
	if oddp(i):
		new_list.append(i)

		
>>> new_list
[1, 3, 5, 7, 9]
>>> sum(l)
45
>>> total = 0
>>> for i in l:
	total +=i

	
>>> total
45
r
>>> reduce (lambda x, y: x+y, l, 0)
45
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sum(l)
45
>>> sum(map(add_ten, filter(oddp, l)))
75
>>> help(oddp)
Help on function <lambda> in module __main__:

<lambda> lambda x

>>> dir(oddp)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> oddp?
SyntaxError: invalid syntax
>>> oddp
<function <lambda> at 0x0000000002C54A58>
>>> [add_ten(i) for i in l if oddp(i)]
[11, 13, 15, 17, 19]
>>> sum ([add_ten(i) for i in l if oddp(i)])
75
>>> help(oddp)
Help on function <lambda> in module __main__:

<lambda> lambda x

>>> dir(oddp)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> function(oddp)0
SyntaxError: invalid syntax
>>> whatis(oddp)

Traceback (most recent call last):
  File "<pyshell#587>", line 1, in <module>
    whatis(oddp)
NameError: name 'whatis' is not defined
>>> inspect(oddp)

Traceback (most recent call last):
  File "<pyshell#588>", line 1, in <module>
    inspect(oddp)
NameError: name 'inspect' is not defined
>>> for name, score in scores:
	print name, score

	
Merlin 123
Nz0 256
DG 1024
>>> {name:key for name, key in scores}
{'Nz0': 256, 'DG': 1024, 'Merlin': 123}
>>> {key:value for key, value in scores)
SyntaxError: invalid syntax
>>> {foo:bar for foo, bar in scores}
{'Nz0': 256, 'DG': 1024, 'Merlin': 123}
>>> dict(scores)
{'Nz0': 256, 'DG': 1024, 'Merlin': 123}
>>> import antigravity
>>> import antigravity
>>> import antigravity
>>> 
>>> 
>>> 
>>> 
>>> import math
>>> math.acos(1)
0.0
>>> math.acos(0.5)
1.0471975511965979
>>> importa cmath
SyntaxError: invalid syntax
>>> import cmath
>>> dir(cmath)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'isinf', 'isnan', 'log', 'log10', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> f = 0.1
>>> f
0.1
>>> f = 0.1 + 0.2
>>> f
0.30000000000000004
>>> f=0.125+0.125
>>> f
0.25
>>> import decimal
>>> fd = decimal.Decimal(10)
>>> fd = 0.3
>>> fd
0.3
>>> fd = 0.000000000000000000003
>>> fd
3e-21
>>> import random
>>> random.randint(1,10)
5
>>> random.choice(names)
'DG'
>>> random.choice(l)
2
>>> random.randint(0,len(names))
2
>>> names[2]
'BV'
>>> c = itertools.count

Traceback (most recent call last):
  File "<pyshell#628>", line 1, in <module>
    c = itertools.count
NameError: name 'itertools' is not defined
>>> c.next())
SyntaxError: invalid syntax
>>> c = itertools.count()

Traceback (most recent call last):
  File "<pyshell#630>", line 1, in <module>
    c = itertools.count()
NameError: name 'itertools' is not defined
>>> import cmath
>>> import math
>>> c = itertools.count()

Traceback (most recent call last):
  File "<pyshell#633>", line 1, in <module>
    c = itertools.count()
NameError: name 'itertools' is not defined
>>> import itertools
>>> c = itertools.count(100)
>>> c.next()
100
>>> c.next)
SyntaxError: invalid syntax
>>> names = []
>>> names = ['merlin], 'dg
	 
SyntaxError: invalid syntax
>>> names = ['merlin', 'dg', 'bv', 'nz0', 'steven', 'a']
>>> colors = ['red', 'blue']
>>> izip(names,ccycle)

Traceback (most recent call last):
  File "<pyshell#642>", line 1, in <module>
    izip(names,ccycle)
NameError: name 'izip' is not defined
>>> itertools.izip(names, ccycle)

Traceback (most recent call last):
  File "<pyshell#643>", line 1, in <module>
    itertools.izip(names, ccycle)
NameError: name 'ccycle' is not defined
>>> itertools.izip(names,ccycle)

Traceback (most recent call last):
  File "<pyshell#644>", line 1, in <module>
    itertools.izip(names,ccycle)
NameError: name 'ccycle' is not defined
>>> import os
>>> 
>>> os.listdir('.')
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'Scripts', 'tcl', 'test.txt', 'Tools']
>>> os.path.basename('some/test/file.ext)
		 
SyntaxError: EOL while scanning string literal
>>> os.path.basename('some/test/file.ext')
'file.ext'
>>> import pickle
>>> scores
(('Merlin', 123), ('Nz0', 256), ('DG', 1024))
>>> p
<__main__.Point object at 0x0000000002BD8C18>
>>> d
{'key': 'value'}
>>> pickle.dump(d,fp)

Traceback (most recent call last):
  File "<pyshell#654>", line 1, in <module>
    pickle.dump(d,fp)
  File "C:\Python27\lib\pickle.py", line 1376, in dump
    Pickler(file, protocol).dump(obj)
  File "C:\Python27\lib\pickle.py", line 224, in dump
    self.save(obj)
  File "C:\Python27\lib\pickle.py", line 286, in save
    f(self, obj) # Call unbound method with explicit self
  File "C:\Python27\lib\pickle.py", line 652, in save_dict
    write(MARK + DICT)
ValueError: I/O operation on closed file
>>> import hashlib
>>> import time
>>> 
