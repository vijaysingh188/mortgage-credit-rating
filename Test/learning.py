class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self.__model = model  # Private attribute

    # Getter for brand
    def get_brand(self):
        return self._brand

    # Setter for brand
    def set_brand(self, brand):
        self._brand = brand

    # Getter for model
    def get_model(self):
        return self.__model

    # Setter for model
    def set_model(self, model):
        self.__model = model

# Creating an object

car = Car("Toyota", "Corolla")
# print(car.get_brand())  # Accessing via getter
# car.set_model("Camry")  # Modifying via setter
print(car.get_model())  # Accessing via getter




# mylist = [1,2,3,5,7,8]

# # output = list(map(lambda x:x**2,filter(lambda x:x%2==0,mylist)))
# # print(output,'=====output')

# output = [{x:x**2} for x in mylist if x %2==0]
# print(output)







# # import pymysql

# # connection = pymysql.connect(host="localhost",'user'='someusee',password='password')

# # cursor = connection.cursor()
# # cursor.execute("CREATE DATABASE NEWDB")
# # cursor.close()
# # connection.close()

def remove_elements(n):
    mylist = list(range(1, n + 1))  # Create a list of people numbered from 1 to n
    remove_even = True  # Start by removing elements at even indices
    
    while len(mylist) > 1:
        if remove_even:
            # Remove elements at even indices
            mylist = [x for i, x in enumerate(mylist) if i % 2 == 0]
        else:
            # Remove elements at odd indices
            mylist = [x for i, x in enumerate(mylist) if i % 2 != 0]
        remove_even = not remove_even  # Toggle between even and odd removals
        
    return mylist[0]  # Return the last remaining person

# Parameters
n = 100  # Total number of people

# Find the last remaining person
last_person = remove_elements(n)
print(f"The last remaining person is {last_person}.")





# mylist = [x for x in range(1,21)]
# print(mylist)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# newlist = [x for i, x in enumerate(mylist) if i % 2 == 0]
# print(newlist) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# newlist = [x for i, x in enumerate(newlist) if i % 2 != 0]
# print(newlist)






