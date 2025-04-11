###############################################
fo = open("foo.txt","rwt")
print("Name of the file:",fo.name)
for index in range(5):
    line = fo.next()
    print("Line No %d - %s ",(index,line))
fo.close()
# output 
# Syntax Error

###############################################
fo = open("foo.txt", "wb")
print("Name of the file",fo.name)
fo.flush()
fo.close()
# # output
# Flushes the file when closing them

##########################
count ={}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
tot=0
for i in count:
    tot = tot+count[i]
 
print(len(count)+tot)
 
# output
# 16
 
#######################
a= {}
print a.fromkeys([1,2,3],"check")
 
# output
# {1: 'check', 2: 'check', 3: 'check'}
 
##########################
a = (0,1,2,3,4)
b = slice(0,2)
print(a[b])

# output
# (0,1)
 
##############
class A:
    pass
class B:
    pass
obj = B()
isinstance(obj,A)
print("True")
 
# output
# True

##########################
class A:
    def __init__(self,x=3):
        self._x = x
class B(A):
    def __init__(self):
        super().__init__(5)
    def display(self):
        print(self._x)
       
def main():
    obj=B()
    obj.display()
   
main()
# output
# 5
 
########################
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y=1
def main():
    b= Derived_Test()
    print(b.x,b.y)
   
main()
# output
# 0 1
       
       
##########################
 
def foo():
    try:
        print(1)
    finally:
        print(2)
foo()
 
#output
# 2
 
#####################################
def f(x):
    for i in range(5):
        yield i
g=f(8)
print(list(g))
# output
# [0, 1, 2, 3, 4]
 
#########################################
def f(x):
    yield x+1
g=f(8)
print(next(g))
output
# 9
 
######################
def f(x):
    yield x+1
    print("test")
    yield x+2
g=f(10)
print(next(g))
print(next(g))
 
# output
# 11
# test
# 12
 
##################
def a():
    try:
        f(x,4)
    finally:
        print('after f')
        print('after f?')
a()
 
# output
# after f
# after f?
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 130, in <module>
#   File "<main.py>", line 126, in a
# NameError: name 'f' is not defined
 
 
########################
class test:
    def __init__(self):
        self.variable = 'Old'
        self.Changes(self.variable)
    def Changes(self,var):
        var='New'
obj=test()
print(obj.variable)
##output
# Old

##################################
class Person:
    def __init__(self,a,b):
        self.name = a
        self.listofcompany = b
    def display(self):
        print("Name",self.name)
        for i in self.listofcompany:
            i.display()
class Company:
    def __init__(self,c,d):
        self.name = c
        self.o = d
    def display(self):
        self.o.display()
        print("Company",self.company)
l=[]
n=3
for i in range(n):
    c=Company(input("Enter the Company "))
    l.append(c)
    p=Person("Jaya",1)
    p.display()
#output
#one-many

##########################
class change:
    def __init__(self,x,y,z):
        self.a=x+y+z
x= change(1,2,3)
y=getattr(x,'a')
setattr(x,'a',y+1)
print(x.a)
#output
#7

##########################
a=range(2,9)
d=map(lambda x,y:x**y,a,reversed(a))
print(d)
# #output
# True

##########################
import numpy as np
A=np.matrix([[1,2],[3,4]])
B=np.mat([[5,6],[5,6]])
C=A*B
print(C)
# output
# A Matrix Product

##########################
import numpy as np
op = np.arange(10)
# print(op)

##########################
list1=[2,33,222,14,25]
print(list1[:-1])
# output
# [2, 33, 222, 14]



from math import gcd

def are_coprime(a, b):
    return gcd(a, b) == 1

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def sum_of_squares_of_digits(n):
    return sum(int(digit)**2 for digit in str(n))

def count_trick_numbers(L, R):
    count = 0
    for num in range(L, R + 1):
        sum_digits = sum_of_digits(num)
        sum_squares = sum_of_squares_of_digits(num)
        if are_coprime(sum_digits, sum_squares):
            count += 1
    return count  # This line should be outside the for loop

L, R = map(int, input().split())
result = count_trick_numbers(L, R)

print(result)




