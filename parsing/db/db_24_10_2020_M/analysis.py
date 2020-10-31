#!/usr/bin/env python3

import pandas as pd
from prettytable import PrettyTable
import glob
import os

x = PrettyTable()
x.field_names = ["Location","TestME","ID","Url","CacheUrl","IP","ASNumber","PingAVG","TimeToGetFirstByte","RedirectUrl","StatusCode"]

filename="global_24_M.csv"
fields=["Location","TestME","ID","Url","CacheUrl","IP","ASNumber","PingAVG","TimeToGetFirstByte","RedirectUrl","StatusCode"]


with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for results in sorted(glob.glob("*.csv")):
        data = pd.read_csv(results, sep=",", header=0)
        #global = data.sort_values('Url', ascending=True))
        #print(data.iloc[31])
        for i in range(len(data)):
           x.add_row(data.iloc[i])
print(x)
    #print(data.groupby(['Url'])['Url'])
