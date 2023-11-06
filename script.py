"""
"""
"""
This script run 
"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import os
import re

user = os.getlogin()
path = f"C:/Users/{user}/MYBB/"
filepath = "Governance"
# filepath = re.sub(r'[^\x00-\x7F]+', '', filepath)
Test_folder = "Test/"
Finance_folder = "Report/"
account_folder = "Account/
Inventory_folder = 'Inventory/

def to_read_files_each(path, filepath, folder_type):
    directory = os.path.join(path,filepath, folder_type)
    if not os.path.exists(directory):
        os.makedirs(directory) # 
    files = os.listdir(directory)
    for file in range(len(files)):
        file_list = files[file] 
        if re.search("Requirement", file_list):
            if folder_type == "Inventory/":
                df = pd.read_excel(directory + file_list,  sheet_name = 1, skiprows = 9)
            else: 
                df = pd.read_excel(directory + file_list,  sheet_name = 0, skiprows = 9)
        df = df.loc[~df["Business Tech Names"].isnull(),:] 
    return df

def to_read_files(path, filepath, folder_type):
    directory = os.path.join(path, filepath, folder_type)
    series_list = []
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for filename in filenames:
            mainpath = os.path.join(dirpath, filename)
            if re.search("Requirement", mainpath):
                test = pd.read_excel(mainpath, skiprows=9)
                series_list.append(test)  # Append the selected column to the list
    concatenated_series = pd.concat(series_list, ignore_index=True)
    dfn = pd.DataFrame(concatenated_series)
    dfn = dfn[~dfn["Business Tech Names"].isnull()]
    return dfn

Test_folder = "Test/"
Finance_folder = "Report/"
account_folder = "Account/
Inventory_folder = 'Inventory/

account = to_read_files_each(path,filepath,account_folder )
Finance = to_read_files_each(path, filepath,Finance_folder )
Test = to_read_files_each(path, filepath,Test_folder )
Inventory = to_read_files(path, filepath, Inventory_folder)

combined_df = pd.concat([Customer, alert, case, List, account], ignore_index=True)
all_ = len(account) + len(Finance) + len(Inventory) + len(Test) 

print("# of Account is: {}".format(len(account)))
print("# of Finance is: {}".format(len(Finance)))
print("# of Test is: {}".format(len(Test)))
print("# of Inventory is: {}".format(len(Inventory)))
print("# of all Total is: {}".format(all_))

if all_ == 137:
    print("validated....consider that archived folder files are included")
else:
    print("Need to take # of rules existing in the excel")
    
    
def preprocessing(combined_df): 
    imprt = combined_df["Technical Desc"].to_list()
    lst = []
    only_one = []
    for i in range(len(imprt)):
        elements = str(imprt[i]).split("\n")[2].split(":")
        if len(elements) > 1:
             lst.append(elements[1])
        else:
            only_one.append(elements[0])
    filler = "not parsed"
    combined_df.loc[:, "tech_terms"] = lst + [filler]*(len(combined_df.index) - len(lst))
    return combined_df
    
preprocessing(combined_df)

