import numpy as np
import pandas as pd
def lol():
    newarray = [1,2,4]
    for i in range(len(newarray)):
        print(i)
        print(newarray[i])
        i+=1

    print("kluar item")
    newarray.pop(0)
    print(newarray)

def pdcreate():
    df = pd.DataFrame()
    df = df.append({1:'lol',2:'omeglul',3:'pog'},ignore_index=True)
    print(df)

def pdc():
    df = pd.DataFrame(columns=('a','b','c'), data=[(1,2,3),(3,4,5)])
    print(df)


pdc()
