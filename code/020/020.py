import threading
import time
import schedule

def hourly_job():
    t = time.strftime("%H:%M:%S", time.gmtime(time.time()))
    print(f"I'm running on thread {threading.current_thread()}")
    print(f"{t}: Did a thing on the hour")

def daily_job():
    t = time.strftime("%H:%M:%S", time.gmtime(time.time()))
    print(f"I'm running on thread {threading.current_thread()}")
    print(f"{t} - Did a thing on the day")

def job_thread(job):
    thread = threading.Thread(target=job)
    thread.start()

if __name__ == "__main__":
    schedule.every(10).seconds.do(job_thread, hourly_job)
    schedule.every(60).seconds.do(job_thread, daily_job)
    
    t = time.strftime("%H:%M:%S", time.gmtime(time.time()))
    print(f"{t} ~ Starting scheduler")
    while 1:
        schedule.run_pending()
        time.sleep(1)

# 22:38:28 ~ Starting scheduler
# I'm running on thread <Thread(Thread-1 (hourly_job), started 140145422452480)>
# 22:38:38: Did a thing on the hour
# I'm running on thread <Thread(Thread-2 (hourly_job), started 140145422452480)>
# 22:38:48: Did a thing on the hour
# I'm running on thread <Thread(Thread-3 (hourly_job), started 140145422452480)>
# 22:38:58: Did a thing on the hour
# I'm running on thread <Thread(Thread-4 (hourly_job), started 140145422452480)>
# 22:39:08: Did a thing on the hour
# I'm running on thread <Thread(Thread-5 (hourly_job), started 140145422452480)>
# 22:39:18: Did a thing on the hour
# I'm running on thread <Thread(Thread-6 (daily_job), started 140145422452480)>
# 22:39:28 - Did a thing on the day
