

def find_substring(nums,sub):
    i = 0

    while i <len(nums)-1:
        if nums[i:i+len(sub)] == sub:
            return i
        i=i+1
    return -1
num = "abaabcabadb"
sub = 'abc'
# print(find_substring(num,sub))


def count_substring(nums,sub):
    count = 0
    i = 0
    while i < len(nums)-1:
        if nums[i:i+len(sub)] == sub:
            count +=1
            i=i+len(sub)
        else:
            i=i+1
    if count == 0:
        return -1
    return count
    
nums = "abcabcabadbabcabc"
sub = 'abc'
# print(count_substring(nums,sub))




def  count_chars(input_string):
    count = 0
    previous = input_string[0]
    i=0
    output = ''
    while i < len(input_string):
        if input_string[i] == previous:
            count +=1
        else:
            output = output + previous+str(count)
            count = 1
            previous =  input_string[i]
        i=i+1
    output = output + previous+str(count)  
    return output

input_string = 'aaabbcccz'
output_string = 'a3b2c3z1'
# print(count_chars(input_string))




def count_chars_via_dict(input_string):
    mydict = {}
    output = ""
    for ele in input_string:
        mydict[ele] = mydict.get(ele,0)+1

    for char,nums in mydict.items():
        output = output + char+str(nums)    
    return output

input_string = 'aaabbcccz'
output_string = 'a3b2c3z1'
# print(count_chars_via_dict(input_string))


def change_nums_in_string(input_string):
    output = ""
    for ele in input_string:
        if ele.isalpha():
            previous = ele            
        else:
            output = output + previous*int(ele)

    return output

input_string = "a3b2c3z1"
output_string = "aaabbcccz"

# print(change_nums_in_string(input_string))

def change_string(input_string):
    output = ""

    for ele in input_string:
        if ele.isalpha():
            previous = ele

        else:
            output = output + previous+chr(ord(previous)+int(ele))
    return output

input_string = "a3b2c3x1"
output_string = "adbdcfxy"

# print(change_string(input_string))


def sort_alpha_digits(input_string):
    alp = []
    digits = []
    for ele in input_string:
        if ele.isalpha():
            alp.append(ele)
        else:
            digits.append(ele)

    output = "".join(sorted(alp)+sorted(digits))
    return output

input_string = "XAC512"
output_string = "ACX125"
# print(sort_alpha_digits(input_string))


