def reverse_list(input_list):
    i = 0
    j = len(input_list)-1
    while i < j:
        input_list[i],input_list[j] = input_list[j],input_list[i]
        i +=1
        j -=1
    return input_list

input_list = [3,2,4,1,0,9]#[9, 0, 1, 4, 2, 3]
# print(reverse_list(input_list))

def max_min(input_list):
    max_ele = input_list[0]
    min_ele = input_list[0]
    for ele in  input_list:
        if ele  > max_ele:
            max_ele = ele
        else:
            min_ele = ele
    return  max_ele,min_ele

# input_list = [3,2,4,1,0,9]
# print(max_min(input_list))

def remove_dup(input_list):
    for ele in input_list:
        if input_list.count(ele) > 1:
            input_list.remove(ele)
    return  input_list

input_list = [0,0,1,1,2]
# print(remove_dup(input_list))

def sort_list(input_list):
    i=0
    while i < len(input_list)-1:
        j=i+1
        while j < len(input_list):
            if input_list[i]>input_list[j]:
                input_list[i],input_list[j] = input_list[j],input_list[i]
            j+=1
        i+=1
    return input_list

input_list = [3,2,4,1,0,9]
# print(sort_list(input_list))


def two_sum(nums,target):
    i=0
    while i < len(nums)-1:
        j=i+1
        while j < len(nums):
            if  nums[i]+nums[j] == target:
                return (i,j)
            j+=1
        i+=1
    return -1


nums =  [2,7,11,15]
target = 13

# print(two_sum(nums,target))


def fib_gen(nums):
    a,b = 0,1
    for _ in range(nums):
        yield a
        a,b = b,a+b
 
# print(list(fib_gen(10)))

def find_prime(nums):
    if nums == 1:
        return False
    if nums >= 2:
        for i in range(2,nums):
            if nums % i == 0:
                return False
        else:
            return True
        
# print(find_prime(nums=19))
nums = 19
# for i in range(1, nums):
#     print(f"{i} is prime: {find_prime(i)}")


##################strng#############
# def find_substring(main_str,sub):
#     i=0
#     while i < len(main_str)-1:
#         if main_str[i:i+len(sub)] == sub:
#             return i
#         else:
#             i+=1
#     return -1
        

# main_str = 'abababcdab'
# sub = 'bcd'
# print(find_substring(main_str,sub))


def count_ss(main_str,sub):
    i=0
    count=0
    while  i < len(main_str)-1:
        if main_str[i:i+len(sub)] == sub:
            count+=1
            i=i+len(sub)
        else:
            i+=1
    return count

main_str = 'abababcdab'
sub = 'ab'
# print(count_ss(main_str,sub))



def count_str(input_string):
    i=0
    previous = input_string[0]
    count = 0
    output=''
    while i <len(input_string):
        if input_string[i] == previous:
            count+=1
        else:
            output = output+previous+str(count)
            previous = input_string[i]
            count=1
        i+=1
    output = output+previous+str(count)
    return output
        
input_string = 'aaabbcccz'
output_string = 'a3b2c3z1'

# print(count_str(input_string))


# n = 5
# # for i in range(nums+1):
# #     for j in range(i):
# #         print("*",end="")
# #     print()
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2 * i - 1)+" "*(n-i))

###########static method,Class method############################
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
    
    
    
obj1 = Stock("laptop",10)
print(obj1.company_name)
# obj1.do_cal("xx",20,10)
# obj1.get_calc(9)
print(obj1.change_name())
print(obj1.company_name)
# print("---------------------")
# obj2 = Stock("mobile",10)
# obj2.get_calc(3)
# print(obj2.company_name)






 






