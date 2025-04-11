# from openpyxl import Workbook

# wb= Workbook()
# ws = wb.active

# header = ['name','city','country']

# data = [
#     ["vj",'hyd','india'],
#     ['kj','newyork','usa'],
#     ['jj','toronto','canada']
#     ]

# ws.append(header)
# for row in data:
#     ws.append(row)

# wb.save('myfile.xlsx')

#################Read excel
# from openpyxl import load_workbook

# # Load the workbook
# wb = load_workbook("newdata.xlsx")

# # Select the active worksheet
# ws = wb.active

# # Read and print the contents of the first row (header)
# header = [cell.value for cell in ws[1]]  # Assuming the header is in the first row
# print(header)

# # Read and print the contents of all rows
# for row in ws.iter_rows(values_only=True):
#     print(row)



############method2

import xlsxwriter

# Create a new Workbook and add a worksheet
workbook = xlsxwriter.Workbook('new_file.csv')
worksheet = workbook.add_worksheet()

# Define the header and data
header = ['Name', 'Age', 'City']
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Write the header to the first row
worksheet.write_row(0, 0, header)

# Write the data rows
for row_num, row_data in enumerate(data, start=1):
    worksheet.write_row(row_num, 0, row_data)

# Close the workbook
workbook.close()



