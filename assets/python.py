# -*- coding: utf-8 -*-
import json
import csv
import datetime
from urllib2 import urlopen
start_date ='2022-05-25'
end_date ='2022-07-05'


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return False
    return True

if validate(start_date) and validate(end_date) :
    weather = urlopen('https://api.github.com/repos/pkar15/watchlist/commits?since={0}T00:00:00Z&until={1}T23:59:59Z'.format(start_date,end_date))
    wjson = weather.read()
    wjdata = json.loads(wjson)
    rows = []
    tr = []
    for i in wjdata:
        tr = [i["sha"],i["commit"]["author"]["name"],i["commit"]["author"]["email"],i["commit"]["author"]["date"]]
        rows.append(tr)
    fields = ['commit id', 'Name', 'Email', 'Date']
    filename ="gitreport.csv"
        
    with open (filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
else :
    print "Please enter correct date format. YY-MM-DD"



