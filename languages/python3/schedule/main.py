import schedule
import time

def job(data=None):
    if data:
        print(data)
    else:
        print("I'm working...")

# By default, every is 1

# Every 15 seconds (so the first is in 15 seconds)
schedule.every(5).seconds.do(job,"yes")

schedule.every().hour.do(job)

schedule.every().day.at("10:12").do(job)

# Random execute between 2 and 3 seconds (2 seconds cycle)
schedule.every(2).to(3).seconds.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)