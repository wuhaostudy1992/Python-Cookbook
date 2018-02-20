import csv
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        #print(r)
        row = Row(*r)
        #print(row)
        
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)
