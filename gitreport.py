import json
import csv
import datetime
from urllib2 import urlopen
#start_date ='2022-05-25'
#end_date ='2022-07-05'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--start_date', default='2022-07-05')
parser.add_argument('--end_date', default='2022-07-06')
parser.add_argument('--repo_url', default='https://github.com/pkar15/watchlist.git')

args = parser.parse_args()

start_date = args.start_date
end_date = args.end_date
repo_url = args.repo_url


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return False
    return True

if validate(start_date) and validate(end_date) :
    url= repo_url[:8] + "api." + repo_url[8:]
    if url.find(".com") != -1:
        index = url.find(".com")
        url = url[:index+5] + "repos/" + url[index+5:]
    if url[-1] == "/":
        url = url[:-1]
    if url.endswith(".git"):
        url = url[:-4]
    print url

    weather = urlopen(url + '/commits?since={0}T00:00:00Z&until={1}T23:59:59Z'.format(start_date,end_date))
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
