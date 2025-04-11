def remove_duplicates(mylist):
    if  not mylist:
        return 0 
    i = 0
    while i < len(mylist):
        j = i+1
        while j < len(mylist):
            if mylist[i] == mylist[j]:
                mylist.pop(j)
            else:
                j=j+1
        i=i+1
    return  mylist

mylist = [5,4,2,0,1,1,2,2,4,5]
# print(remove_duplicates(mylist))

# mylist = [5,4,2,0,1,1,2,2,4]
# newlist = []

# for i in mylist:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)


def two_sum(nums,target):
    i = 0
    while i < len(nums):
        j = i+1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return  [i,j]
            else:
                j=j+1
        i=i+1
    return -1

nums = [2,7,9,11]
target = 18

# print(two_sum(nums,target))

def reverse_list(nums):
    i = 0
    j = len(nums)-1
    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i = i+1
        j = j-1
    return nums

nums = [3,4,1,2,0]
# print(reverse_list(nums))

def sort_list(nums):
    i = 0
    while i < len(nums)-1:
        j =i+1
        while j < len(nums):
            if  nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                j=j+1
        i=i+1
    return nums

nums = [3,4,0,1,6]
# print(sort_list(nums))


def rotate_list(nums,k):
    nums = nums[k:] + nums[:k] 
    return nums

nums = [0,1,2,3,4,5]
k =3
# print(rotate_list(nums,k))


def count_ele(nums):
    mydict = {}

    for ele in nums:
        mydict[ele]  = mydict.get(ele,0) +1

    max_key = max(mydict,key=lambda x:mydict[x])
    print(max_key)

    min_key = min(mydict,key=lambda x:mydict[x])
    print(min_key)


    return mydict

nums = [0,1,2,3,4,5,2,1,0,5,1,1,1,1,0]
# print(count_ele(nums))


def max_ele(nums):
    i = 0 
    temp = nums[0]
    while i < len(nums)-1:
        if nums[i] > temp:
            temp = nums[i]
        i=i+1
    return temp

nums = [2,0,1,5,10,4,5]
# print(max_ele(nums))
def group_elements_by_target(mylist, target):
    finallist = []
    i = 0

    while i < len(mylist):
        temp_list = []
        current_sum = 0

        while i < len(mylist) and current_sum + mylist[i] <= target:
            current_sum += mylist[i]
            temp_list.append(mylist[i])
            i += 1

            # Break the inner loop if we reach the target sum
            if current_sum == target:
                break

        finallist.append(temp_list)

        # If the current_sum exactly matches the target, we don't increment `i` again
        if current_sum != target:
            i += 1  # Continue from the next element if the target wasn't exactly met

    return finallist

# Input list and target sum
mylist = [1, 2, 2, 3, 0, 5, 2, 1, 2]
target = 5

# Group the elements and print the result
finallist = group_elements_by_target(mylist, target)
print(finallist)



# def find_array(mylist,target):
#     finallist = []
#     temp_list = ''
#     i=0
#     while i < len(mylist):
#         j=i+1
#         while j < len(mylist):
#             if mylist[i]+mylist[j] == target:
#                 temp_list = temp_list +  str(mylist[i]) +',' + str(mylist[j]) 

#                 finallist.append(temp_list)
#                 temp_list = ''
#             else:
#                 j=j+1
#             i=i+1
#     return  finallist



# mylist = [1,2,2,3,0,5,2,1,2]
# finallist = [[1,2,2],[2,3],[5],[2,1,2]]
# target = 5

# print(find_array(mylist,target))

# 381492053547


def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = 10
fib_series = list(fibonacci_generator(n))
print(fib_series)
   