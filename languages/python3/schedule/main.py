import schedule
import time

def job(data=None):
    if data:
        print(data)
    else:
        print("I'm working...")

# By default, every is 1

jobs = []
# Every 15 seconds (so the first is in 15 seconds)
jobs.append(schedule.every(5).seconds.do(job,"yes"))

jobs.append(schedule.every().hour.do(job))

jobs.append(schedule.every().day.at("10:12").do(job))

# Random execute between 2 and 3 seconds (2 seconds cycle)
jobs.append(schedule.every(2).to(3).seconds.do(job))

i = 0
while i < len(jobs):
    print("Jobs {} : {}".format(i, jobs[i]))
    i+=1


while 1:
    schedule.run_pending()
    time.sleep(1)