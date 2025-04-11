# n = 5
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print('*',end="")
# #     print()

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# n = 4
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))

# for i in range(n, 0, -1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))
# # n = 4
# # for i in range(1, n + 1):
# #     print(' ' * (n - i) +  str(i) * (2 * i - 1))

# # n = 4
# # for i in range(1, n + 1):
# #     print(' ' * (n - i) + ' '.join(str(i) for _ in range(i)))

# n = 5
# for i in range(1, n + 1):
#     print(' ' * (n - i) + ' '.join(chr(64 + i) for _ in range(i)))


# # n = 4
# # for i in range(n - 1, 0,-1):
# #     print(' ' * (n - i) + '*' * (2 * i - 1))
# # for i in range(1, n + 1):
# #     print(' ' * (n - i) + '*' * (2 * i - 1))

# n = 5
# num =1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num = num+1
#     print()


# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n =4
# for i in range(1,n+1):
#     print("*"*i +" "*(2*(n-i))+"*"*i)
# for i in range(n,0,-1):
#     print("*"*i +" "*(2*(n-i))+"*"*i)




# n = 4
# for i in range(1, n + 1):
#     print(" "*(n-i)+str(i)*(2 * i - 1)+" "*(n-i))

# for i in range(n,0,-1):
#     print(" "*(n-i)+str(i)*(2 * i - 1)+" "*(n-i))


#######pascal triange
# n = 5
# for i in range(n):
#     print(" " * (n - i), end="")
#     coef = 1
#     for j in range(i + 1):
#         print(coef, end=" ")
#         coef = coef * (i - j) // (j + 1)
#     print()



# import re
# ip_patterrn = r'\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\b'
# ip_addresses = '192.168.1.1'
# check = re.match(ip_patterrn,ip_addresses)
# if check:
#     print('s')
# else:
#     print('no')


# def check_pal(ss):
#     return ss==ss[::-1]


# def check_string(input_data):
#     output =""
#     max_length =0
#     i=0
    
#     while i < len(input_data):
#         j=i
#         while j<len(input_data):
#             substring= input_data[i:j+1]
#             if check_pal(substring):
#                 if len(substring) > max_length:
#                     max_length=len(substring)
#                     output = substring
#             j=j+1
#         i=i+1 
#     return output



# input_data= 'ababadab'
# print(check_string(input_data))



# def check_pal(ss):
#     return ss==ss[::-1]


# def check_string(input_data):
#     output =""
#     max_length =0
#     for i in range(len(input_data)):
#         for j in range(i,len(input_data)):
#             substring = input_data[i:j+1]
#             if check_pal(substring):
#                 if len(substring)>max_length:
#                     max_length = len(substring)
#                     output = substring
#     return output


# input_data= 'mada'
# print(check_string(input_data))


# #############data is csv
import pandas as pd
from multiprocessing import Pool
 
# Function to process a single chunk
def process_chunk(chunk):
    # Calculate total revenue per category
    chunk['revenue'] = chunk['quantity'] * chunk['price']
    category_revenue = chunk.groupby('category')['revenue'].sum()
    return category_revenue
 
# Function to process the entire file with parallel processing
def calculate_total_revenue(file_path, chunk_size, output_file):
    results = []
    with Pool(processes=4) as pool:  # Adjust the number of processes
        # Read the file in chunks and process in parallel
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            results.append(pool.apply_async(process_chunk, args=(chunk,)))
 
        # Collect results from all processes
        aggregated_results = pd.concat([r.get() for r in results])
 
    # Final aggregation
    total_revenue = aggregated_results.groupby(aggregated_results.index).sum()
 
    # Sort by total revenue in descending order
    total_revenue = total_revenue.sort_values(ascending=False)
 
    # Write the result to a new CSV file
    total_revenue.to_csv(output_file, header=["total_revenue"])
    print(f"Output written to {output_file}")
 
# Example usage
if __name__ == "__main__":
    file_path = "large_file.csv"
    chunk_size = 100000  # Adjust the chunk size based on your system's memory
    output_file = "category_revenue.csv"
    calculate_total_revenue(file_path, chunk_size, output_file)



# ##################excel data
# from openpyxl import load_workbook
# import pandas as pd
# from multiprocessing import Pool
 
# # Function to process a single chunk of rows
# def process_chunk(chunk):
#     # Convert the chunk to a DataFrame
#     df = pd.DataFrame(chunk, columns=["category", "quantity", "price"])
#     # Ensure correct data types
#     df["quantity"] = pd.to_numeric(df["quantity"])
#     df["price"] = pd.to_numeric(df["price"])
    
#     # Calculate total revenue per category
#     df["revenue"] = df["quantity"] * df["price"]
#     category_revenue = df.groupby("category")["revenue"].sum()
#     return category_revenue
 
# # Function to read an Excel file incrementally and process it with multiprocessing
# def process_large_excel_with_pool(file_path, sheet_name, chunk_size, output_file):
#     results = []
#     workbook = load_workbook(file_path, read_only=True)
#     sheet = workbook[sheet_name]
 
#     with Pool(processes=4) as pool:  # Adjust the number of processes
#         # Read rows in chunks
#         chunk = []
#         for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):  # Skip the header
#             chunk.append(row)
#             if len(chunk) == chunk_size:
#                 # Submit the chunk to the pool for processing
#                 results.append(pool.apply_async(process_chunk, args=(chunk,)))
#                 chunk = []
 
#         # Process any remaining rows
#         if chunk:
#             results.append(pool.apply_async(process_chunk, args=(chunk,)))
 
#         # Collect results from all processes
#         aggregated_results = pd.concat([r.get() for r in results])
 
#     # Final aggregation
#     total_revenue = aggregated_results.groupby(aggregated_results.index).sum()
 
#     # Sort by total revenue in descending order
#     total_revenue = total_revenue.sort_values(ascending=False)
 
#     # Write the result to a new Excel file
#     total_revenue.to_excel(output_file, header=["total_revenue"])
#     print(f"Output written to {output_file}")
 
# # Example usage
# if __name__ == "__main__":
#     file_path = "large_file.xlsx"
#     sheet_name = "Sheet1"
#     chunk_size = 1000  # Adjust the chunk size based on memory
#     output_file = "category_revenue.xlsx"
#     process_large_excel_with_pool(file_path, sheet_name, chunk_size, output_file)

# def decorator_func(func):
#     def wrapper_func(a,b):
#         if b == 0 :
#             return "0 is not divisible"
#         else:
#             return func(a,b)
#     return wrapper_func



# @decorator_func
# def divide_func(a,b):
#     return a//b


# print(divide_func(15,0))



# import time
# def time_decorator(func):
#     def wrapper_func(*args):
#         st = time.time()
#         result = func(*args)
#         et = time.time()
#         print("time diff is",et-st)
#         return result
#     return wrapper_func




# @time_decorator
# def cal_sum(*args):
#     return sum(args)

# print(cal_sum(10,20,30))




# class Emp:
#     def parent_method(self):
#         print("its a parent method")

# class Programmer(Emp):
#     # def parent_method(self):
#     #     print("its a chlld method")

#     def child_method(self):
#         print("its child class")
#         super().parent_method()

# obj = Programmer()
# obj.child_method()
# # obj.parent_method()

class Bank:
    bank_name = "ABC"
    def __init__(self,Account_number,Account_balance=None):
        self.Account_number =Account_number
        self.Account_balance =Account_balance

    
    
    def change_bankname(cls):
        cls.bank_name = "XYZ"
        return cls.bank_name
    
    def show_balance(self):
        return self.Account_balance
    
    @staticmethod
    def do_cal(Account_balance,amt):
        if Account_balance <= amt:
            return "Insufficient Balance"
        return Account_balance - amt

    def debit(self,amount):
        result = self.do_cal(self.Account_balance, amount)
        if isinstance(result, str):  # If the result is a message, return it
            return result
        else:
            self.Account_balance = result  # Update the balance
            return self.show_balance()


        
    def credit(self,amount):
        self.Account_balance += amount
        return self.show_balance()  


    
p1 = Bank(12345,1000)
# print(p1.bank_name)
# print(p1.change_bankname())
# print(p1.bank_name)
# print(p1.show_balance())
print(p1.debit(200))
# print(p1.credit(3000))






































































