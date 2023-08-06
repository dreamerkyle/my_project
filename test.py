import numpy as np 
import pandas as pd
import os

def import_excel(file_path):
    os.chdir("/Users/kylezh/Desktop/myzone")
    df = pd.read_excel(file_path)
    print(df)

if __name__=="__main__":
    
    file_path = "testingdata.xlsx"
    import_excel(file_path)
    a = 1
    b = 2
    d = 4
    c = 3
