import pandas as pd
import numpy as np

list1 = pd.read_excel(r"C:\Users\Admin\Documents\Book2.xlsx") # SAP EXCEL
list2 = pd.read_excel(r"C:\Users\Admin\Documents\Book1.xlsx") # EXCEL

def py_data_finder1 (l1, l2):
	i = 0
	print("LIST OF MATCHING DATA")
	for index, row in l1.iterrows():
		for undex, now in l2.iterrows():
			if (index == undex )and (l2.at[i,'Order'] <= l1.at[i,'Order']):
				print("access")
				i += 1
        # return list(row)

def py_data_finder2 (l1, l2):
	i = 0
	print("LIST OF NON-MATCHING DATA")
	for index, row in l1.iterrows():
		for undex, now in l2.iterrows():
			if (index == undex )and (l2.at[i,'Order'] >= l1.at[i,'Order']):
				print("reject")
				i += 1
        # return list(row)
py_data_finder1(list1, list2)
py_data_finder2(list1, list2)
