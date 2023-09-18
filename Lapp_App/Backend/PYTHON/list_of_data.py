# # LIST OF list_matching_data AND list_non_matching_data BY TAKING INPUT FROM USER
# import pandas as pd
# import numpy as np
#
# df = pd.read_excel(r"C:\Users\Admin\Documents\coois.xlsx")
#
# def py_data_finder(element, available_list):
#     print("\n\t\t\t\t\t\t\t\t\t  LIST OF MATCHING DATA \n")
#     for index, row in df.iterrows():
#         if(row['Material Number'] == element):
#             print(list(row))
#     # return list(row)
#     print("\n\t\t\t\t\t\t\t\t\t LIST OF NON MATCHING DATA \n")
#     for index, row in df.iterrows():
#         if(row['Material Number'] != element):
#             print(list(row))
#     # return list(row)
# Material Number=int(input())
# print(py_data_finder(Material Number, df))

#    return (list_matching_data, list_non_matching_data)
# have to return the data for both matching and non_matching with multiple tables


# LIST OF list_matching_data AND list_non_matching_data BETWEEN 2 EXCEL SHEETS
import pandas as pd
import numpy as np

list1 = pd.read_excel(r"C:\Users\Admin\Downloads\coois.xlsx") # SAP EXCEL
list2 = pd.read_excel(r"C:\Users\Admin\Downloads\expeiment.xlsx") # EXCEL

def py_data_finder1( list1, list2):
    print("\n\t\t\t\t\t\t\t\t\t  LIST OF MATCHING DATA \n")
    for index, row in list1.iterrows():
        for undex, now in list2.iterrows():
            if index == undex and row['Order'] == now['Order']:
                print(list(row))
        # return list(row)
def py_data_finder2(list1, list2):
    print("\n\t\t\t\t\t\t\t\t\t  LIST OF NON-MATCHING DATA \n")
    for index, row in list1.iterrows():
        for undex, now in list2.iterrows():
            if index == undex and row['Order'] != now['Order']:
                print(list(row))
        # return list(row)

py_data_finder1(list1, list2)
py_data_finder2(list1, list2)
