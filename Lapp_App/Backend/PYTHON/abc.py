import pandas as pd
import numpy as np
from functions import fetch_WO
col_list=['Order','Material Number','Material description','Order quantity (GMEIN)','Delivered quantity (GMEIN)']
list1 = pd.read_excel(r"C:\Users\Admin\Downloads\expeiment.xlsx",usecols=col_list) # SAP EXCEL
w_order_db=fetch_WO()
# print(w_order_db)
# for x in w_order_db:
#     print(x[0])
# print(int(x) for x in w_order_db)
b=[int(x[0]) for x in w_order_db]
print(b)
# non_match = []
# for i in sap_list:
#     if i not in w_order_db:
#         non_match.append(i)
# print(b)
def py_data_finder1( list1, b):

    print("\n LIST OF MATCHING DATA \n")
    for index, row in list1.iterrows():
        for now in b:
            if row['Order'] == now:
                print(list(row))
        # return list(row)
def py_data_finder2(list1, b):
    print("\n  LIST OF NON-MATCHING DATA \n")
    for index, row in list1.iterrows():
        for now in w_order_db:
            if row['Order'] != now:
                print(list(row))
        # return list(row)

py_data_finder1(list1,b)
py_data_finder2(list1,b)
