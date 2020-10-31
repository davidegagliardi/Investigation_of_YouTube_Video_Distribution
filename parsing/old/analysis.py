#!/usr/bin/env python3

import pandas as pd
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Location","TestME","ID","Url","CacheUrl","IP","ASNumber","PingAVG","TimeToGetFirstByte","RedirectUrl","StatusCode"]

data = pd.read_csv('america_e_db_1.csv', sep=",", header=0)
#data.sort_values('Url', ascending=True))
#print(data.iloc[31])
for i in range(len(data)):
    x.add_row(data.iloc[i])
#     print("ciao")
print(x)
#print(data.groupby(['Url'])['Url'])
