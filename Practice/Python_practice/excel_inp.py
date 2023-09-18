import pandas as pd
from functions import fetch_WO
from functions import updatedb
from functions import updatingqty
def WO_Excel_Input_py(file_location):
    try:
        col_list=['Order','Material Number','Material description','Order quantity (GMEIN)','Delivered quantity (GMEIN)']
        wo_sap_sheet = pd.read_excel(file_location,usecols=col_list)
        # df=pd.DataFrame(wo_sap_sheet)
        # print(df.values.tolist())
        # b=df.values.tolist()
        # print(b)
        w_order_db=fetch_WO()
        list_of_tuples =w_order_db
        list_of_lists = [list(elem) for elem in list_of_tuples]
        print(list_of_lists)
        b=[int(x[0]) for x in w_order_db]
        # c=[int(x[3]) for x in w_order_db]
        # a=list(wo_sap_sheet['Order'])
        # sap_list = [str(x) for x in a]
        match_sap=[]
        # match_db=[]
        # print("\n\t\t\t\t\t\t\t\t\t  LIST OF MATCHING DATA \n")
        for index, row in wo_sap_sheet.iterrows():
            if row["Order"] in b:
                # print(list(row))
                match_sap.append(list(row))
        # print(match_sap)
        non_match = []
        # print("\n\t\t\t\t\t\t\t\t\t LIST OF NON MATCHING DATA \n")
        for index, row in wo_sap_sheet.iterrows():
            if row["Order"] not in b:
                # print(list(row))
                non_match.append(list(row))
        q=non_match
        updatedb(q)
        # print(non_match)
        qty=[]
        for i in match_sap:
            for j in list_of_lists:
                j[0]=int(j[0])
                if(i[0]==j[0]):
                    print("hi")
                    y=i[3]-i[4]
                    if(y<=j[4]):
                        print("yes")
                        updatingqty(y,j[0])
                    else:
                        print("NO")

        # print(qty)

        # print(non_match)
        # b=[int(x) for x in non_match]
        # print(b[0])
        # c=list(df["Order"])
        # for i in b:
        #     for j in c:
        #         if i==j:
        #             print(i)
        # return non_match
        # for i in non_match:
        #     q=df.loc[df['Order']==non_match[i]]
        #     tuple(q)
        #     f_non_match.append(q)
        # print(f_non_match)

        # for i in w_order_db:
        #     if i not in sap_list:
        #         non_match.append(i)

        # for i in sap_list:
        #     for i in non_match:
        #         rslt_df = df[df['Order'] == non_match]
        # print(rslt_df)

        # def returnNotMatches(a, b):
        #     return [[x for x in a if x not in b], [x for x in b if x not in a]]
        # non_match = returnNotMatches(sap_list, w_order)
        # return 0

    except ValueError:
        return [False,'Columns are wrong']

    except FileNotFoundError:
        return [False,'Not an excel file']

path=["C:\\Users\\Admin\\Downloads\\expeiment.xlsx"]
a=WO_Excel_Input_py(path[0])
print(a)
