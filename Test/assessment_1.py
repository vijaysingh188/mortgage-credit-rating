# class Demo:
#     def __init__(self):
#         __a =1
#         self.__b =1
#         self.__c =1
#         __d__ =1

# output
# self.__b  and self.__C

# fo = open("foo.txt","rw+")
# print("Name of the file:",fo.name)
# for index in range(5):
#     line = fo.next()
#     print("Line No %d - %s ",(index,line))
# fo.close()
# output 
# Syntax Error

# fo = open("foo.txt", "wb")
# print("Name of the file",fo.name)
# fo.flush()
# fo.close()
# # output
# Flushes the file when closing them


# count ={}
# count[(1,2,4)] = 5
# count[(4,2,1)] = 7
# count[(1,2)] = 6
# count[(4,2,1)] = 2
# tot=0
# for i in count:
#     tot = tot+count[i]
 
# print(len(count)+tot)
 
# output
# 16

# A= {1:"A",2:"B",3:"C"}
# print(A.get(1))
# # output
# # A


# import numpy as np
# print(np.__version__)

a = (0,1,2,3,4)
b = slice(0,2)
print(a[b])