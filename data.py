import csv

class security(object):
    def __init__(self,row):
        self.Cusip = row[0]
        self.SecurityType = row[1]
        self.Rate = float(row[2])

filename = "/home/claudio/Downloads/securityprice.csv"
conn = open(filename)
data = csv.reader(conn)
for row in data:
    a = security(row)
    b = a.Rate