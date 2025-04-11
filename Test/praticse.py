# # input_list =[1,3,2,4,8,5]
# # i=0
# # j = len(input_list)-1
# # while i < j:
# #     input_list[i],input_list[j] = input_list[j],input_list[i]
# #     i=i+1
# #     j=j-1
# # print(input_list) 

# ############ find max and min number from list
# # input_list =[1,3,2,4,8,5]
# # max_value = input_list[0]
# # min_value = input_list[0]
# # for ele in input_list:
# #     if ele > max_value:
# #         max_value = ele
# #     if ele < min_value:
# #         min_value = ele
# # print(max_value,min_value)


# #####remove duplicated
# # input_list =[1,3,2,4,8,5,1,2,4]
# # new_list = []
# # for ele in input_list:
# #     if ele not in new_list:
# #         new_list.append(ele)

# # print(new_list)

# # input_list =[1,3,2,4,8,5,1,2,4]
# # i=0
# # while i < len(input_list):
# #     ele = input_list[i]
# #     if input_list.count(ele)>1:
# #         input_list.remove(ele)
# #     else:
# #         i=i+1

# # print(input_list)




# ######Count the ele frequency and largest key and who holds max value
# # input_list =[1,3,2,4,8,5,1,2,4]

# # mydict ={}

# # for ele in input_list:
# #     mydict[ele] = input_list.count(ele)

# # print(mydict,max(mydict))
# # print(max(mydict,key=lambda k:mydict[k]))

# ######Two Sums

# # def two_Sums(input_list):
    
# #     target = 21
# #     i=0
# #     while i < len(input_list)-1:
# #         j=i+1
# #         if input_list[i] + input_list[j] == target:
# #             print(i,j)
# #         else:
# #             j=j+1
# #         i=i+1
# #     return None

# # input_list = [2,7,9,11]
# # two_Sums(input_list)

# #String


# # def count_substring(string,substring):
# #     count = 0
# #     i=0

# #     while i < len(string):
# #         if string[i:i+len(substring)] == substring:
# #             count = count+1
# #             i = i +len(substring)
# #         else:
# #             i=i+1
# #     print(count)

# # count_substring("abdabdab","ab")




# # input_ele = 'ababab'
# # output = 3
# # print(count_string(input_ele))

# # def reverse_string(s):
# #     output = s.split()[::-1]
# #     return  ' '.join(output)


# # s= 'who am i'
# # print(reverse_string(s))


# def longest_common_prefix(strs):
#     # If the list is empty, return "-1"
#     if not strs:
#         return "-1"

#     # Sort the list of strings
#     strs.sort()

#     # Get the first and last strings after sorting
#     first = strs[0]
#     last = strs[-1]
#     min_length = min(len(first), len(last))

#     i = 0
#     # Find the common prefix between the first
#     # and last strings
#     while i < min_length and first[i] == last[i]:
#         i += 1

#     # Check if there's no common prefix
#     if i == 0:
#         return "-1"

#     # Return the common prefix
#     return first[:i]

# strs = ["geeksforgeeks", "geeks", "geek", "geezer"]
# print("The longest common prefix is:",
#       longest_common_prefix(strs))

# def get_number(num):
#     if num > 1:
#         for i in range(2,num):
#             if num%i==0:
#                 return False
#         else:
#             return True
#     return False


# # get prime number from 1 t0 50
# mylist = [x for x in range(51)]
# # print(mylist)
# def check_all_numbers(mylist):
#     prime_numbers = []
#     for ele in mylist:
#         if get_number(ele):
#             prime_numbers.append(ele)
#     return prime_numbers        

# print(check_all_numbers(mylist))


# class Student:
#     def __init__(self):
#         pass
        
#     def details(self,name,age,qualification):
#         self.age = age
#         self.name = name
#         self.qualification = qualification

#         return  self.name,self.age,self.qualification


# s1 = Student()
# print(s1.details("vijay","32","BE"))


# def reverse_string(strs):
#     pass
# input = "HelloWorld"
# output = str(list(reversed(input)))

# output = input[::-1]
# print(output)



# db.user.find({"username":"vijay"})
# import monkey
# class A:
#      def func(self):
#           print ("func() is called")



# def monkey_func(self):
# 	print ("monkey_func() is called")

# # replacing address of "func" with "monkey_func"
# monkey.A.func = monkey_func
# obj = monkey.A()

# # calling function "func" whose address got replaced
# # with function "monkey_func()"
# obj.func()











# class Emp:
#     def parent_method(self):
#         print("its a parent method")

# class Programmer(Emp):
#     # def parent_method(self):
#     #     print("its a chlld method")

#     def child_method(self):
#         print("its child class")
#         # super().parent_method()

# obj = Programmer()
# obj.child_method()
# obj.parent_method()




# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Progammer(Employee):
#     def __init__(self,name,age,lang):
#         super().__init__(name,age)
        
#         self.lang = lang
 
# class Progammer(Employee):
#     def __init__(self,name,age,lang):
#         self.name = name
#         self.age = age
#         self.lang = lang

# obj1 = Employee('vijay',30)
# print(obj1.name,obj1.age)

# obj2 =  Progammer('akash',25,'python')
# print(obj2.name,obj2.age,obj2.lang)



# class Amount:
#     def __init__(self, account_number,balance):
#         self.account_number = account_number
#         self.balance =  balance

#     def credit(self,amount):
#         self.balance += amount
#         print("Amount credited successfully",amount)
#         self.show_balance()

#     def debit(self,amount):
#         if  amount < self.balance:
#             self.balance -= amount 
#             print("amount debited sucessfully",amount)
#             self.show_balance()

#         else:
#             print("Insufficient balance")
        
        

#     def show_balance(self):
#         print("Account balance:",self.balance)

# c1 = Amount("11122",10000)
# c1.credit(5000)
# c1.debit(2000)


# class parentclass:
#     def __init__(self):
#         self._a = 2

# class childclass(parentclass):
#     def __init__(self):
#         super().__init__()
#         print("calling protect member of parent class",self._a)

#         self._a = 3
#         print("calling public member of child class",self._a)

# obj = childclass()

# obj2  = parentclass()
# print(obj2._a)


# class Base:
#     def __init__(self):
#         self.a = "its a"
#         self.__c = "its c"

# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print("Calling private member of base class: ")
#         print(self.__c)


# # Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1.__c)

# obj1 = Derived()
# print(obj1.__c)




# Brand: Maruti
# Model: Alto
# Year: 2022
# Speed up ...
# Not having this feature


# from abc import ABC,abstractmethod

# class  Car(ABC):
#     def __init__(self,brand,color,model):
#         self.brand = brand
#         self.color = color
#         self.model = model

#     @abstractmethod
#     def print_details(self):
#         pass

#     def acc(self):
#         print("car is accelerated")

#     def appliies_break(self):
#         print("car is stopped")

# class Xuv(Car):
#     def print_details(self):
#         print("brand :",self.brand)
#         print("color:",self.color)
#         print("Model:",self.model)

#     def sunroof(self):
#         print("sunroof not available")

# class Suv(Car):
#     def print_details(self):
#         print("brand :",self.brand)
#         print("color:",self.color)
#         print("Model:",self.model)

#     def sunroof(self):
#         print("sunroof is available")


# obj = Car("Tata","Red",'experia')
# obj.acc()

# obj1 = Suv("Tata","Red",'experia')
# obj1.print_details()
# obj1.acc()
# obj1.appliies_break()
# obj1.sunroof()


# @staticmethod and @classmethod

# from abc import ABC,abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         print("------------do something----------")
# class Laptop(Computer):
#     def process(self):
#         return super().process()
#         # print("Laptop clss")

# obj =  Computer()
# obj.process()


# class topTen:
#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
        
# obj  = topTen()

# for i in obj:
#     print(i)



# def my_generator(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 1

# for i in my_generator(5):
#     print(i)


# import threading

# def cube_root(n):
#     print(n**3)

# def square_root(n):
#     print(n**2)

# obj1 = threading.Thread(target=cube_root,args=(3,))
# obj2 = threading.Thread(target=cube_root,args=(13,))

# obj1.start()
# obj2.start()

# obj1.join()
# obj2.join()

# import multiprocessing

# def cube_root(n):
#     print(n**3)

# def square_root(n):
#     print(n**2)

# obj1 = multiprocessing.Process(target=cube_root,args=(2,))
# obj1.start()
# obj1.join()


# def count_substring(s):
#     count = 0
#     i = 0
#     substring = "ab"

#     while i < len(s):
#         if s[i:i+len(substring)] == substring:
#             count =count +1
#             i = i+len(substring)

#         else:
#             i=i+1

#     return count


# s= "abababab"
# print(count_substring(s))


# def reverse_string(s):
#     output = reversed(s)
#     output = ''.join(output)

#     return output


# s= "whoami"

# print(reverse_string(s))

# def reverse_string(s):
#     s =" ".join(s.split()[::-1]) 
#     print(s)

#     return s


# s= "Learing python is very easy"
# expected = "easy very is python learning"

# reverse_string(s)
    
# def reverse_string(s):
#     s1= s.split()
#     print(s1)
#     l1 = []
#     for word  in s1:
#         l1.append(word[::-1])

#     finalop = " ".join(l1)
#     print(finalop)

# s= "durga soft"
# expc = "agurd tfos"

# reverse_string(s)

# def revere_even_string(input):
#     s1  =  input.split()
#     l1 = []
#     i = 0
#     while i  < len(s1):
#         if i % 2 == 0:
#             l1.append(s1[i])
#         else:
#             l1.append(s1[i][::-1])

#         i=i+1

        
#     output = " ".join(l1)
#     print(output)

# input = "one two three four"
# # output = "one owt three ruof"
# revere_even_string(input)


# def sort_ch(s):
#     alp_list = []
#     dig_list = []

#     for ch in s:
#         if ch.isalpha():
#             alp_list.append(ch)

#         else:
#             dig_list.append(ch)

#     output = "".join(sorted(alp_list)+sorted(dig_list))
#     print(output)



# s= "DBA765"
# expc ="ABD567"
# sort_ch(s)

# def make_str(input):
#     final_op = ''
#     for ch in input:
#         if ch.isalpha():
#             previous = ch
#         else:
#             final_op = final_op + int(ch)*previous

#     print(final_op)
# input = "a4b2z3"
# output = 'aaaabzzz'

# make_str(input)


# def make_string(input):
#     finalop =''
#     previous = input[0]
#     count = 1
#     i = 1

#     while i < len(input):
#         if input[i] == previous:
#             count += 1
#         else:
#             finalop = finalop + str(count) + previous
#             previous =  input[i]
#             count = 1

#         if i == len(input)-1:
#             finalop = finalop + str(count) + previous

#         i=i+1
#     print(finalop)

    
# input = "aaaabbccc"
# output = '4a2b3c'

# make_string(input)



# def make_str(input):
#     finalop = ''

#     for ch in input:
#         if ch.isalpha():
#             previous = ch
#         else:
#             finalop = finalop + previous + chr(ord(previous)+int(ch))

#     print(finalop)

# input = "a1d3c1"
# output = 'abdgcd'
# make_str(input)


# def ocuu_string(input):
#     mydict ={}
#     finalop=''
#     for  ch in input:
#         mydict[ch] = mydict.get(ch,0)+1

#     print(mydict)
#     for k,v in sorted(mydict.items()):
#         finalop = finalop +str(v)+k
#     print(finalop)

# input = 'aaaabbccc'
# output = {'a':4,'b':2,'c':3}
# ocuu_string(input)



# mylist = lambda x,y : x+y

# output = [x**2 for x in range(1,11) if x %2 ==0]
# # output = [(x,x**2)for x in range(1,11) if x %2 ==0]
# print(output)

# def mydecorator_func(func):
#     def  wrapper(a,b):
#         if b  == 0:
#             return func(b,a)
#         return  func(a,b)
#     return wrapper

# @mydecorator_func   
# def divison_func(a,b):
#     return a/b


# print(divison_func(10,0))


# pip install pymongo

# from pymogo import Mongoclient

# client = Mongoclient("mongodb://localhost:27017")

# db = client['mydatabase']
# collection = db['mycollection']

# document = {}
# collection.insert_one(document)


# @staticmethod and @classmethod and @property


# class student:
#     def __init__(self, name, phy,math,chem):
#         self.name  = name
#         self._phy = phy
#         self.math = math
#         self.chem = chem
#     @property
#     def phy(self):
#         return  self._phy

#     def cal_avg(self):
#         avg =  (self.phy + self.math + self.chem)/3
#         return avg
    
# obj1  = student("Arun",50,70,79)
# print(obj1.cal_avg())
# obj1._phy = 100
# print(obj1.cal_avg())


# class Student:
#     # Class attribute
#     school_name = "ABC High School"

#     def __init__(self, name, phy, math, chem):
#         self.name = name
#         self.phy = phy
#         self.math = math
#         self.chem = chem

#     @property
#     def average(self):
#         """Calculate and return the average of the three subjects."""
#         return (self.phy + self.math + self.chem) / 3

#     @staticmethod
#     def is_passing(marks):
#         """Determine if the given marks pass the threshold."""
#         return all(mark >= 35 for mark in marks)

#     @classmethod
#     def set_school_name(cls, new_name):
        
#         cls.school_name = new_name

#     @classmethod
#     def get_school_name(cls):

#         return cls.school_name

# # Create an instance of the Student class
# student1 = Student("Arun", 50, 70, 79)

# # Access the average property
# print(f"{student1.name}'s average: {student1.average}")
# # Arun's average: 66.33333333333333

# # Static method usage
# marks = [80, 20, 90]
# print(f"Are the marks {marks} passing? {'Yes' if Student.is_passing(marks) else 'No'}")
# # Are the marks [50, 70, 79] passing? Yes

# # Class method usage
# print(f"Current school name: {Student.get_school_name()}")
# # Current school name: ABC High School

# # Change the school name using class method
# Student.set_school_name("XYZ Academy")
# print(f"Updated school name: {Student.get_school_name()}")
# Updated school name: XYZ Academy


# sales = [
#   { "item": "apple", "quantity": 10, "price": 1.5 },
#   { "item": "orange", "quantity": 5, "price": 2.0 },
#   { "item": "apple", "quantity": 7, "price": 1.5 },
#   { "item": "banana", "quantity": 12, "price": 1.0 },
#   { "item": "orange", "quantity": 8, "price": 2.0 }
# ]


# query = db.sales.aggregate([
#     {$group:{
#         _id: "$item",
#         total:{$sum:"$quantity"},
#         avgprice:{$avg:"$price"}
#     }}
# ])

# db.sales.aggregate([
#   {
#     $group: {
#       _id: "$item",                     // Group by item field
#       totalQuantity: { $sum: "$quantity" }, // Sum of quantities
#       averagePrice: { $avg: "$price" }      // Average price
#     }
#   }
# ])
 

# def prime_number(num):

#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 # print(num,"Not prime number")
#                 break
            
#         else:
#             print(num,'Its prime number')

# def given_number(n):
#     for i in range(n):
#         prime_number(i)


# n = 23
# given_number(n)

###########static method,Class method############################
# class Stock:
#     company_name = "ABC"
#     def __init__(self,type_of_object,number_of_object):
#         self.type_of_object = type_of_object
#         self.number_of_object = number_of_object

#     @staticmethod
#     def do_cal(x,y,z):
#         if z >y:
#             print("Not Enough object to provide") 
#         else:
#             y -= z
#             print("Object provided",y)

#     @classmethod
#     def change_name(cls):
#         cls.company_name = "XYZ"
#         return  cls.company_name

    
#     def get_calc(self,required_supply):
#         self.do_cal(self.type_of_object,self.number_of_object,required_supply)

#     def show_report(self):
#         print(self.number_of_object) 
    
    
    
# obj1 = Stock("laptop",10)
# print(obj1.company_name)
# obj1.get_calc(9)
# print(obj1.change_name())
# print(obj1.company_name)
# print("---------------------")
# obj2 = Stock("mobile",10)
# obj2.get_calc(3)
# print(obj2.company_name)


# import re
# ip = r"\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[1-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[1-9])\b"
# input_ip = '192.168.1.32'
# obj = re.match(ip,input_ip)
# if obj:
#     print("Valid IP")
# else:
#     print("not valid")





# def check_sub(sub):
#         return sub == sub[::-1]


# def check_palindrome(str_inp):
#     output = ""
#     max_length = 0

#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             substring = s[i:j + 1]
#             if is_palindrome(substring):
#                 if len(substring) > max_length:
#                     max_length = len(substring)
#                     longest_palindrome = substring
    
#     # i = 0
#     # while i < len(str_inp):
#     #     j=i
#     #     while j <len(str_inp):
#     #         substring = str_inp[i:j+1]
#     #         if check_sub(substring):
#     #             if max_length < len(substring):
#     #                 max_length = len(substring) 
#     #                 output = substring 
#     #         j=j+1
#     #     i=i+1

#     return output





# I have a file my_file.csv. 
# I want to read this as series as this has only one column in it.


# import pandas as pd
# import csv

# with open("my_file.csv",'r') as f:
#     f = pd.series(f)

# import pandas as pd

# # Read the CSV file into a DataFrame
# df = pd.read_csv('my_file.csv', header=None)

# # Convert the DataFrame to a Series (assuming the DataFrame has only one column)
# series = df.iloc[:, 0]

# # Print the Series
# print(series)


# mylist = [{x:x**2} for x in range(1,10) if x%2 ==0 ]
# mylist = [{x: (lambda y: y**2)(x)} for x in range(1, 10) if x % 2 == 0] ####to get dict
# mylist = [(x, (lambda y: y**2)(x)) for x in range(1, 10) if x % 2 == 0] ####to get tuple
# [(2, 4), (4, 16), (6, 36), (8, 64)] 

# mylist = [{x:x**2} if x%2 ==0 else {x:x} for x in range(1,10)]
# mylist = [{x: (lambda y: y**2)(x)} if x % 2 == 0 else {x: (lambda y: y)(x)} for x in range(1, 10)]
# mylist = [(x, (lambda y: y**2)(x)) if x % 2 == 0 else (x, (lambda y: y)(x)) for x in range(1, 10)]
# [(1, 1), (2, 4), (3, 3), (4, 16), (5, 5), (6, 36), (7, 7), (8, 64), (9, 9)] 




























# mylist = [[5,4,3],[2,0,2],[1,1,1]]

# output = [[2,0],[1,1],[5,4]]
# sorted_list = sorted(mylist ,key=lambda x :x[2])
# print(sorted_list,'=====sorted_list')




# Write a function for a given a string str, 
# find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example1:
# Input: str = "netapp"
# Output: 0
# Example2:
# Input: str = "netappnetapp"
# Output: -1
# Example3:
# Input: str = "lovenetapplove"
# Output: 4




# def input_funct(input):
#     previou = input[0]
#     i=0
#     while i < len(input):
#         if input[i] == previou:
#             i += 1
#         return input[i]
# input = "netapp" 
# input_funct(input)



















