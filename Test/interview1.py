# import pandas as pd
# import numpy as np
# import csv

# data = pd.read_csv("pandasdata.csv",header=None)
# data.columns = ['Name', 'Age', 'City']
# df = pd.DataFrame(data)
# df['Country'] = ['Ind','Ind','USA','Canada']
# # df['new_age']  = df['Age'].apply(lambda x:x+10)

# # filter_data = df[(df['Age']>30) & (df['Country']!="Ind")]
# # print(filter_data)

# # print(df)

# data2 ={
#     'Name':['Akash','Ganesh'],
#     'Age':[29,np.nan],
#     'City':['chennai','Lahore'],
#     'Country':['Ind','Pak']
        
# }
# df2 = pd.DataFrame(data2)
# # print(df2)

# # new_df_concat = pd.concat((df,df2),axis=0,ignore_index=True)
# # print(new_df_concat)

# # df2 = df2.rename(columns={"Age":"Age1","City":"Sub_city"})


# df2 = df2.fillna({'Age':40})
# print(df2)

# # df_left = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
# # df_right = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
# # df_merged = pd.merge(df_left, df_right, on='key', how='inner') #'left','right',outer
# # print(df_merged)


# import numpy as np

# mylist = [10,4,1,2,3]
# np_arary = np.array(mylist)

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# # print(arr_2d)

# np_data = np.arange(1,4)
# # print(np_data)
# arr = np.random.rand(3, 4)
# # print(arr)

# arr = np.array([1, 2, 3, 4, 5, 6])
# reshaped_arr = arr.reshape((2, 3))
# # print(reshaped_arr)
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# dot_result = np.dot(arr1, arr2)       # Matrix multiplication
# matmul_result = np.matmul(arr1, arr2) # Also matrix multiplication

# arr = np.array([[1, 2], [3, 4]])
# flat_arr = arr.flatten()    # Output: array([1, 2, 3, 4])
# print(flat_arr)
# mylist = [[10,4],[1,2,3]]
# list_comp = [x for y in mylist for x in y]
# print(list_comp)

# n =5
# # for i in range(n+1):
# #     for j in range(1,i):
# #         print('*',end="")
# #     print()

# # for i in range(n+1):
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1)+" "*(n-i))



# from openpyxl import Workbook

# workbook = Workbook()
# ws = workbook.active
# header = ['Name','Age','City']
# data = [
#     ['A','B','C'],
#     [10,20,30],
#     ['P','Q','R']
# ]
# ws.append(header)
# for row in  data:
#     ws.append(row)

# workbook.save("newdata.xlsx")

# from openpyxl import load_workbook

# # Load the workbook
# workbook = load_workbook("newdata.xlsx")

# # Select the active worksheet
# ws = workbook.active

# # Read and print the contents of the first row (header)
# # header = [cell.value for cell in ws[1]]  # Assuming the header is in the first row
# # print(header)

# # Read and print the contents of all rows
# for row in ws.iter_rows(values_only=True):
#     print(row)



#######database
# from pymongo import mongolclient
# client = pymongo.mongoclient("db://localhost:27017")
# document = client['document_name']
# collection = document['document']
# data = {}
# collection.insertOne(data)
# client.close()

# import psycopg2

# connection = psycopg2.connect(
#     database='postgres',
#     user='username',
#     password ='*****',
#     host='localhost',
# )
# cursor = connection.cursor()
# query ="SELECT * FORM DATATABE"

# cursor.execute(query)
# cursor.close()
# connection.close()

#####remove duplicate records
# import numpy as np
# import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', np.nan],
#     'Age': [25, np.nan, 35],
#     'City': ['New York', 'Los Angeles', np.nan]
# }
# df = pd.DataFrame(data)

# # df.loc[[0, 1], 'Age'] = [45, 55]
# df.iloc[[0,1], 1] = [45, 55]
# print(df)
# # # df.iloc[1, 1] = 55
# # df.iloc[[0,1], 1] = [45, 55]


# class Base:
#     def __init__(self):
#         self.a = "its a"
#         self.__c = "its c"

# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print("Calling private member of base class: ")
#         print(self.__c)


# # Driver code
# obj1 = Base()
# print(obj1.a)
# print(obj1._Base__c)

# # obj1 = Derived()
# print(obj1.__c)


# import re
# ip =r'\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\b'

# # ip = r"\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[1-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[1-9])\b"
# input_ip = '192.168.1.32'
# obj = re.match(ip,input_ip)
# if obj:
#     print("Valid IP")
# else:
#     print("not valid")




# def find_max_profit_mul_trans(prices):
#     if not prices:
#         return 0 
#     max_profit =0
#     for i in range(1,len(prices)):
#         if prices[i]> prices[i-1]:
#             print(prices[i],prices[i-1])
#             max_profit += prices[i]-prices[i-1]
#     return max_profit
    

# prices = [7,1,5,3,6,4]
# print(find_max_profit_mul_trans(prices))


# def max_profit_one_trans(prices):
#     if not prices:
#         return 0 
        
#     min_price = float("inf")
#     max_profit = 0
#     for price in prices:
#         min_price = min(min_price,price)
#         profit = price - min_price
#         max_profit = max(max_profit,profit)
#     return max_profit
        
        
# prices = [7,1,5,3,6,4]
# print(max_profit_one_trans(prices))


# def find_largest(mylist):
#     import heapq
#     n=2
#     mynumber = heapq.nlargest(n,mylist)[1]
#     print(mynumber)


# mylist = [7,1,5,3,6,4]
# find_largest(mylist)




# def knapsack_dp_optimized(values, weights, capacity):
#     n = len(values)
#     # Initialize a 1D DP array
#     dp = [0] * (capacity + 1)
#     print(dp,len(dp))

#     # Fill the DP array
#     for i in range(n):
#         for w in range(capacity, weights[i] - 1, -1):
#             dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

#     return dp[capacity]

# # Example usage
# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
# print(knapsack_dp_optimized(values, weights, capacity))  # Output: 220

# class Calculator:
#     def __init__(self):
#         # You could keep a history of operations or results if needed
#         self.result = 0
    
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             raise ValueError("Cannot divide by zero")
#         return a / b

#     def calculate(self, operator, a, b):
#         # Map operators to corresponding methods
#         operations = {
#             '+': self.add,
#             '-': self.subtract,
#             '*': self.multiply,
#             '/': self.divide
#         }
        
#         if operator not in operations:
#             raise ValueError(f"Invalid operator '{operator}'")
        
#         # Call the relevant method dynamically
#         return operations[operator](a, b)


# # Usage example
# calc = Calculator()

# try:
#     a, b = 10, 5
#     print("Addition:", calc.calculate('+', a, b))
#     print("Subtraction:", calc.calculate('-', a, b))
#     print("Multiplication:", calc.calculate('*', a, b))
#     print("Division:", calc.calculate('/', a, b))
# except ValueError as e:
#     print(e)




# class calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def add_operation(self):
#         return self.a + self.b
    
#     def mul_operator(self,*args):
#         return self.a*self.b
    
# obj = calculator(10,5)
# result = obj.add_operation()
# print(obj.mul_operator(result))









#######################practise##############
# def remove_dups(mylist):
#     i=0
#     while i < len(mylist):
#         j=i+1
#         while j < len(mylist):
#             if mylist[i] == mylist[j]:
#                 mylist.pop(j)
#             else:
#                 j=j+1
#         i=i+1
#     return mylist


# mylist = [7,1,5,3,6,4,5,7]
# print(remove_dups(mylist))

# def sort_list(nums):
#     i = 0
#     while i < len(nums)-1:
#         j =i+1
#         while j < len(nums):
#             if  nums[i] > nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#             else:
#                 j=j+1
#         i=i+1
#     return nums

# nums = [7,1,5,3,6,4]
# print(sort_list(nums))

# def sort_list(mylist):
#     i=0
#     while i < len(mylist)-1:
#         j=i+1
#         while j < len(mylist):
#             if mylist[i] > mylist[j]:
#                 mylist[i],mylist[j] = mylist[j],mylist[i]
#             else:
#                 j=j+1
#         i=i+1

#     return mylist

# mylist = [7,1,5,3,6,4]
# print(sort_list(mylist))


# def count_ele(mylist):
#     mydicts = {}
#     for ele in mylist:
#         mydicts[ele] = mydicts.get(ele,0)+1
#     # return mydicts
#     print(mydicts)

#     # max_ele = max(mydicts,key=lambda x:mydicts[x])
#     # return max_ele

#     for key,value in mydicts.items():
#         if value == max(mydicts.values()):
#             print(key)

# mylist = [1,2,1,2,8,9,0,3]
# print(count_ele(mylist))




# def max_number(mylist):
#     max_num = mylist[0]
#     i=0
#     while i < len(mylist):
#         if mylist[i] > max_num:
#             max_num = mylist[i]
#         else:
#             i=i+1
#     return max_num

# print(max_number(mylist=[1,2,4,5,8,3]))


# def two_sum(mylist,target):
#     i=0
#     tar_list =[]
#     while i < len(mylist)-1:
#         j=i+1
#         while j < len(mylist):
#             if mylist[i]+mylist[j] == target:
#                 tar_list.append([i,j])
            
#             j=j+1
#         i=i+1
#     return tar_list

# print(two_sum(mylist=[1,2,4,3,6],target=7))


# def feba_gen(nums):
#     a,b=0,1
#     for _ in range(nums):
#         yield a
#         a,b=b,a+b


# print(list(feba_gen(nums=10)))


# def string_rotation(mystring):
#     # split_string = " ".join(mystring.split()[::-1])
#     split_string = mystring.split()
#     output=[]
#     for index,ele in enumerate(split_string):
#         if index%2 == 0:
#             output.append(ele[::-1])
#         else:
#             output.append(ele)

#     return " ".join(output)

# mystring = 'vijay kumar singh'
# print(string_rotation(mystring))


# mylist = [1,2,3,5,7,8]

# # # output = list(map(lambda x:x**2,filter(lambda x :x%2==0,mylist)))
# # # print(output)

# output = [x**2 for x in mylist if x%2==0]
# print(output)


# import pymysql

# connection = pymysql.connect(host="localhost:8000",user="username",password="password")
# cursor = connection.cursor()
# cursor.execute("CREATE DATABASE NEWDB")
# cursor.close()
# connection.close()


# import pymongo

# connection = pymongo.MongoClient("mongodb://localhost:27017/")
# database = connection["mydatabase"]
# collection = database["Orders"]
# collection.insert_one({"name":"vijay","age":25})
# connection.close()


class Stock:
    company_name = "ABC"
    def __init__(self,type_of_object,number_of_object):
        self.type_of_object = type_of_object
        self.number_of_object = number_of_object

    @staticmethod
    def do_cal(x,y,z):
        if z >y:
            print("Not Enough object to provide") 
        else:
            y -= z
            print("Object provided",y)

    @classmethod
    def change_name(cls):
        cls.company_name = "XYZ"
        return  cls.company_name

    
    def get_calc(self,required_supply):
        self.do_cal(self.type_of_object,self.number_of_object,required_supply)

    def show_report(self):
        print(self.number_of_object) 
    
    
    
# obj1 = Stock("laptop",10)
# print(obj1.company_name)
# obj1.do_cal("xx",20,10)
# obj1.get_calc(9)
# print(obj1.change_name())
# print(obj1.company_name)
# print("---------------------")
# obj2 = Stock("mobile",10)
# obj2.get_calc(3)
# print(obj2.company_name)



# class Bank:
#     bank_name = "ABC"
#     def __init__(self,Account_number,Account_balance=None):
#         self.Account_number =Account_number
#         self.Account_balance =Account_balance

    
    
#     def change_bankname(cls):
#         cls.bank_name = "XYZ"
#         return cls.bank_name
    
#     def show_balance(self):
#         return self.Account_balance
    
#     @staticmethod
#     def do_cal(Account_balance,amt):
#         if Account_balance <= amt:
#             return "Insufficient Balance"
#         return Account_balance - amt

#     def debit(self,amount):
#         # self.do_cal(amount)
#         result = self.do_cal(self.Account_balance, amount)
#         if isinstance(result, str):  # If the result is a message, return it
#             return result
#         else:
#             self.Account_balance = result  # Update the balance
#             return self.show_balance()


        
#     def credit(self,amount):
#         self.Account_balance += amount
#         return self.show_balance()  


    
# p1 = Bank(12345,1000)
# # print(p1.bank_name)
# # print(p1.change_bankname())
# print(p1.show_balance())
# print(p1.debit(200))
# print(p1.credit(3000))
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# df= pd.concat([df1,df2],axis=1) 
# df = df.fillna(0)
df = pd.merge(df1,df2,on='A',how='outer')
print(df)

# data = {
#     'Name': ['Alice', 'Bob', np.nan],
#     'Age': [25, np.nan, 35],
#     'City': ['New York', 'Los Angeles', np.nan]
# }


# df = pd.DataFrame(data)
# print(df)
# print('-----------------')
# df_sort = df.sort_values(by="Age",ascending= True)
# print(df_sort)

# df.loc[[0, 1], 'Age'] = [45, 55]
# print(df)
# # df.iloc[1, 1] = 55
# df.iloc[[0,1], 1] = [45, 55]
# print(df)



























