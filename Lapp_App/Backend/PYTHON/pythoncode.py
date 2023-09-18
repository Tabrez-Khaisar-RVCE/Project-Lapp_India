import pandas as pd

coois = pd.read_excel(r"C:\Users\Admin\Downloads\expeiment.xlsx")

def countx(coois,x):
    for index, row in coois.iterrows():
        if(row['Material Number'] != x):
            print(list(row))
order_no=int(input())
print(countx(coois, order_no))
