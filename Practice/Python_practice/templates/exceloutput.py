from openpyxl import Workbook

new_list = [["COLUMN NAME1", "COLUMN NAME 2"],["first", "second"], ["third", "fourth"]]

wb = Workbook() # creates a workbook object.
ws = wb.active # creates a worksheet object.

for row in new_list:
    ws.append(row) # adds values to cells, each list is a new row.
a="C:\\Users\\Admin\\Desktop\\File_Name.xlsx"
wb.save(a)
