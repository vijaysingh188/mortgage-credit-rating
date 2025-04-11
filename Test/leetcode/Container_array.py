# Given an array container[], where each element represents the height of a vertical line at that index,
#  find two lines that together with the x-axis form a container that holds the maximum amount of water.
###########Brute force with time complexity:O[n^2]################

def max_area_cal(container):
    maxarea =0
    i=0
    while i < len(container):
        j=i+1
        while j < len(container):
            height = min(container[i],container[j])
            width = j-i
            area = height*width
            maxarea = max(area,maxarea)
            j=j+1
        i=i+1
    return maxarea

container = [7,1,2,3,4]
# print(max_area_cal(container))

def max_area_cal(container):
    maxarea =0
    for i in range(0,len(container)):
        for j in range(i,len(container)):
            height = min(container[i],container[j])
            width = j-i
            area = height*width
            maxarea = max(area,maxarea)
    return maxarea

container = [7,1,2,3,9]
# print(max_area_cal(container))


##########Optimal soultion with time complexity:O[n]
def max_area_cal(container):
    
    maxarea =0
    i=0
    j = len(container)-1
    while i < j:
        height = min(container[i],container[j])
        width = j-i
        area = height*width
        maxarea = max(area,maxarea)
        i=i+1
    return maxarea


container = [7,1,2,3,9]
# print(max_area_cal(container))

