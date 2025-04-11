import csv


# data = [
#     ["Order_ID","Product", "Quantity","Order_Date","Customer_ID"],
#     [101,"Laptop",2,800,"2024-01-15","C001"],
#     [102,"Mouse",5,20,"2024-02-10","C002"],
#     [103,"Keyboard",3,50,"2024-01-20","C003"],
#     [104,"Monitor",1,300,"2024-03-05","C001"],
#     [105,"Laptop",1,850,"2024-02-25","C004"],
# ]

data = [
    ["Customer_ID", "Name", "Age","Location","Gender"],
    ["C001","John Doe",35,"New York","Male"],
    ["C002","Jane Smith",28,"Chicago","Female"],
    ["C003","Sam Brown",42,"Houston","Male"],
    ["C004","Lisa Ray",31,"New York","Female"],
    ["C005","Alex Kim",29,"Los Angeles","Male"],
]


# Creating a CSV file

with open("customer_data.csv", "w", newline="") as file:#sales_data.csv
    writer = csv.writer(file)
    writer.writerows(data)  # Writing multiple rows at once

print("CSV file created successfully!")


