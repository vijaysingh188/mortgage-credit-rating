def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome_brute_force(s):
    n = len(s)
    max_length = 0
    longest_palindrome = ""

    i = 0
    while i < n:
        j = i
        while j < n:
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > max_length:
                max_length = len(substring)
                longest_palindrome = substring
            j += 1
        i += 1 
    return longest_palindrome

# Example Usage
s = "babad"
print("Longest Palindromic Substring:", longest_palindrome_brute_force(s))





def check_list(mylist):
    max_ele = max(mylist)
    min_ele = min(mylist)
    print(max_ele,min_ele)
    i=0
    while i < len(max_ele) and i < len(min_ele) and max_ele[i] == min_ele[i]:
        i=i+1
    return max_ele[:i]

mylist = ["flight", "flow", "flower","fow"] ####output = "fl"
# print(check_list(mylist))


def group_anagrams(strs):
    anagrams = {}
    for ele in strs:
        sorted_str = "".join(sorted(ele))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        
        anagrams[sorted_str].append(ele)
    return list(anagrams.values())

# # Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"] ####[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# print(group_anagrams(strs))

# Input: ["level", "hello", "racecar", "python", "madam"]
# Output: ["level", "racecar", "madam"]

def check_palindrome(ss):
    return ss[::-1] == ss

def check_strings(mylist):
    new_list = []
    for ele in mylist:
        if check_palindrome(ele):
            new_list.append(ele)
    return new_list

mylist = ["level", "hello", "racecar", "python", "madam"]
# print(check_strings(mylist))

def check_vowels(mylist):
    vowel_ele = "aeiou"
    new_list = []
    for ele in mylist:
        if (ele == vowel_ele) or  (ele in vowel_ele) or (ele.lower() in vowel_ele):
            new_list.append(ele)
            
    return new_list
mylist =  ["aeiou", "hello", "EIOU", "python"] ####["aeiou", "EIOU"]

# print(check_vowels(mylist))



def frequent_ele(mylist):
    mydict = {}
    for ele in mylist:
        mydict[ele] = mydict.get(ele,0)+1
    return max(mydict,key=mydict.get)

mylist = ["dog", "cat", "dog", "fish", "cat", "dog"]###dog
# print(frequent_ele(mylist))



def check_numeric(ele):
    for item in ele:
        if item.isdigit():
            return False
    return True


def remove_numeric(mylist):
    final_list = []
    for ele in mylist:
        if check_numeric(ele):
            final_list.append(ele)
    return final_list   


mylist =  ["hello", "world123", "python", "abc99"]# Output: ["hello", "python"]
# print(remove_numeric(mylist))


# Input: "abc"
# Output: ["a", "b", "c", "ab", "bc", "abc"]

def create_ss(Input):
    final_list = []
    i=0
    while i < len(Input):
        j=i+1
        while j < len(Input)+1:
            final_list.append(Input[i:j])
            j=j+1
        i=i+1
    return final_list
Input =  "abc"
print(create_ss(Input))####["a", "b", "c", "ab", "bc", "abc"]

