# coding: utf-8
#
# Programme to convert google myactivity (data.json) to CSV file

import json
import csv
import datetime

with open('data.json', encoding="utf-8") as f:
    datas = json.load(f)

with open("data.csv", "w+", encoding='utf8') as csvfile:
    spamwriter = csv.writer(
        csvfile,
        delimiter=';',
        quotechar='|',
        quoting=csv.QUOTE_MINIMAL)

    # Write CSV Header, If you dont need that, remove this line
    spamwriter.writerow(["data", 'time,' "header", "title", "titleUrl"])

    titleUrl = ''
    after = datetime.datetime(2018, 10, 22)

    for d in datas:

        if 'titleUrl' in d.keys():
            titleUrl = d['titleUrl']
        else:
            titleUrl = ''
        try:
            date = datetime.datetime.strptime(
                d['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
        except:
            date = datetime.datetime.strptime(d['time'], '%Y-%m-%dT%H:%M:%SZ')
        if date < after:
            continue
        row = [str(date.date()), str(date.time()),
               d["header"], d["title"], titleUrl]

        spamwriter.writerow(row)
