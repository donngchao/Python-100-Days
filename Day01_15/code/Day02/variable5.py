"""
类型转换

Version: 0.1
Author: tester
Date: 2019-11-25
"""
#use the function type() to get the variable's type
a = 100
print(a)#100
print(type(a))#<class 'int'>
b = str(a)
print('the value of b is:',b)#the value of b is: 100
print(type(b))#<class 'str'>
c = 12.345
print('the value of c is:',c)
print('the type of c is:',type(c))
"""
the value of c is: 12.345
the type of c is: <class 'float'>
"""
d = str(c)
print('the value of d is:',d)
print('the type of d is:',type(d))
'''
the value of d is: 12.345
the type of d is: <class 'str'>
'''

e = '123'
print('the value of e is:',e)
print('the type of e is:',type(e))
'''
the value of e is: 123
the type of e is: <class 'str'>
'''
f = int(e)
print('the value of f is:',f)
print('the type of f is:',type(f))
'''
the value of f is: 123
the type of f is: <class 'int'>
'''
g = '123.456'
print('the value of g is:',g)
print('the type of g is:',type(g))
'''
the value of g is: 123.456
the type of g is: <class 'str'>
'''
h = float(g)
print('the value of h is:',h)
print('the type of h is:',type(h))
'''
the value of h is: 123.456
the type of h is: <class 'float'>
'''
i = False
print('the value of i is:',i)
print('the type of i is:',type(i))
'''
the value of i is: False
the type of i is: <class 'bool'>
'''
j = str(i)
print('the value of j is:',j)
print('the type of j is:',type(j))
'''
the value of j is: False
the type of j is: <class 'str'>
'''
k = 'hello'
print('the value of k is:',k)
print('the type of k is:',type(k))
'''
the value of k is: hello
the type of k is: <class 'str'>
'''
m = bool(k)
print('the value of m is:',m)
print('the type of m is:',type(m))
'''
the value of m is: True
the type of m is: <class 'bool'>
'''

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(m)
print(type(m))
'''
100
<class 'int'>
100
<class 'str'>
12.345
<class 'float'>
12.345
<class 'str'>
123
<class 'str'>
123
<class 'int'>
123.456
<class 'str'>
123.456
<class 'float'>
False
<class 'bool'>
False
<class 'str'>
hello
<class 'str'>
True
<class 'bool'>

'''

complex_number = 34 + 56j  #This is a complex number.
print(complex_number)
print(type(complex_number))

'''
(34+56j)
<class 'complex'>
'''

test_string = "hello,world" #This is a string.
print(test_string)
print(type(test_string))
'''
hello,world
<class 'str'>
'''