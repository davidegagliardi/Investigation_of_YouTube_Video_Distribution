
#!/usr/bin/env python3

import sqlite3
import glob
import os
import re
import datetime
import time
import pandas as pd
import csv

list_instances=['aalto','america','australia','tokyo']
type_test="m"

fields=["Location","TestME","ID","Url","CacheUrl","IP","ASNumber","PingAVG","TimeToGetFirstByte","RedirectUrl","StatusCode"]

for inst in range (len(list_instances)):
    filename="%s_%s_db_1.csv" % (list_instances[inst], type_test)

    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        #for results in sorted(glob.glob('../databases/*.db')):
        for results in sorted(glob.glob("%s/*.db" % list_instances[inst] )):
            print(results)
            date_tmp = re.findall(r'\d+', results)
            array_date = list(map(str, date_tmp))
            year=array_date[0]
            month=array_date[1]
            day=array_date[2]
            hour=array_date[3]
            minute=array_date[4]
            second=array_date[5]

            #establish connection to debug
            try:
                conn = sqlite3.connect(results)
                selection = ("SELECT * FROM pytomo_crawl_%s_%s_%s_%s_%s_%s") % (year, month, day, hour, minute, second)
                cur = conn.cursor()
                cur.execute(selection)
                rows = cur.fetchall()
                print("INIZIO DATABASE")
                #print("rows",rows)
                if not rows:
                    print("Empty")
                    line = ["%s" % list_instances[inst],"%s" % type_test,"null","null","null","null","null","null","null","null","null"]
                    print(line)
                    csvwriter.writerow(line)
                else:
                    for row in rows:
                        line = ["%s" % list_instances[inst],"%s" % type_test,row[0],row[2],row[3],row[5],row[8],row[10],row[25],row[27],row[28]]
                        print(line)
                        csvwriter.writerow(line)
                conn.close()
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
