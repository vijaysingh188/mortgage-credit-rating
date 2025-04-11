import csv
import pandas as pd
import numpy as np

# df = pd.read_excel('new_file.xlsx')
# print(df.head())

# data = [
#     ['Alice', 25, 'New York'],
#     ['Bob', 31, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago']
# ]

# df = pd.DataFrame(data,columns=['Name', 'Age', 'City'])
# # df = df.rename(columns={"Name":"FullName","Age":"C_Age"})
# # names = df['Name']
# print(names)
# get_name_age = df[['Name','Age']]
# # print(get_name_age)
# get_age = df[df["Age"]>30]


# get_age = df[(df["Age"]>30 )& (df['Name']=='Bob')]
# print(get_age)

# apply_funct = df["Age"].apply(lambda x :x+10)
# print(apply_funct)

# apply_func= df['City'].apply(lambda x : "".join(x.split(" ")[0]))
# print(apply_func)

# import pandas as pd
# import numpy as np

# # Create a DataFrame with missing values
# data = {
#     'Name': ['Alice', 'Bob', np.nan],
#     'Age': [25, np.nan, 35],
#     'City': ['New York', 'Los Angeles', np.nan]
# }


# df = pd.DataFrame(data)


# df_filled = df.fillna({"Name":"Unknown","Age":0,"City":"Unknown"})
# df_filled = df.fillna(0)

# drop_col = df.dropna(subset=["Age"])
# print(drop_col)

# print(df_filled)

# df_dropped = df.dropna()
# print(df_dropped)

# df_sorted = df.sort_values(by="Age",ascending=True)

# print(df_sorted)


# df['Country'] = ["Ind","USA","Canada"]
# print(df)


# df= pd.read_excel('new_file.xlsx') 
# print(df)
# print("-------------------------------------------")
# # df = df.rename(columns={"Name":"FullName","Age":"C_Age"})
# # print(df)
# df['New_age'] = df["Age"].apply(lambda x : x+50)
# print(df)
# print("-------------------------------------------")

# df['sub_age'] = df['New_age'] - df ['Age']
# print(df)
# print("-------------------------------------------")

# # df = df.drop('New_age', axis=1)
# # print(df)

# df = df.rename(columns={"Age":"Age1","sub_age":"sub_age2"})

# print(df)

# print("---------------")
# print(df.head(3))
# print(df)

# print("---------------")

# rows,column = df.shape
# print(rows,column)
# print("============================")

# df.at[0,"Age"] = 45
# # print(df)

# df.loc[2,"Age"] = 60


# df.loc[[0, 1], 'Age'] = [45, 55]
# print(df)
# # df.iloc[1, 1] = 55
# df.iloc[[0,1], 1] = [45, 55]

# # increase_age = df["Age"].apply(lambda x : x**2)

# # output = list(map(lambda x:x**2,filter(lambda x:x%2==0,mylist)))
# # print(increase_age)
# print(df)

# print("---------------")

# # print(df[['Age','City']])
# fileter_df =df[df["Age"]>50] 
# # print(fileter_df)

# df_sort = df.sort_values(by="Age",ascending= False)
# print(df_sort)


# df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# df= pd.concat([df1,df2],ignore_index=True)#axis=0-concats horizontally ,axis=1 -- concats vertically
# # df = df.fillna(0)
# print(df)

# group_by = df1.groupby('A').sum()
# print(group_by)

df_left = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df_right = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
df_merged = pd.merge(df_left, df_right, on='key', how='inner') #'left','right',outer
print(df_merged)

# df_left = pd.DataFrame({'A': [1, 2]}, index=['K0', 'K1'])
# df_right = pd.DataFrame({'B': [3, 4]}, index=['K1', 'K2'])

# # Using join()
# df_join = df_left.join(df_right, how='outer') #left,right,inner
# print(df_join)


 
#                                      Data structure

# primitive                              nonprimitive
#                                           liner                                   non-linear
# string                        directaccess        sequential           hierarchical         unordered 
# float                         matrix             linked list                 Trees           Graphs
# boolean                       array               stack                                       sets
# integer                                            queues

 