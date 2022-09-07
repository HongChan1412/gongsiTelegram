from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
import gongsi_crawl
import telegram_send
import time

def job():
  try:
    print("공시 크롤링 시작")
    res = gongsi_crawl.get_gongsi()
    print("공시 크롤링 완료")
    if res:
      print("공시가 존재함")
      telegram_send.send_msg(res)
      print("메시지 전송 완료")
    else:
      print("공시가 존재하지 않음")
  except Exception as e:
    print(e)

def main():
  try:
    print("""
  ___              _  _     _____  _               _        
  |_  |            (_)| |   /  ___|| |             | |       
    | | _   _  ___  _ | | __\ `--. | |_  _   _   __| | _   _ 
    | || | | |/ __|| || |/ / `--. \| __|| | | | / _` || | | |
/\__/ /| |_| |\__ \| ||   < /\__/ /| |_ | |_| || (_| || |_| |
\____/  \__,_||___/|_||_|\_\\____/  \__| \__,_| \__,_| \__, |
                                                        __/ |
                                                      |___/       
""")
    sched = BackgroundScheduler(timezone='Asia/Seoul')
    sched.start()
    try:
      sched.add_job(job, 'interval', minutes=1, id="gongsiBot", misfire_grace_time=600)
    except:
      try:
        print("기존 Job 제거 후 새로 추가")
        sched.remove_all_jobs()
        sched.add_job(job, 'interval', minutes=1, id="gongsiBot", misfire_grace_time=600)
      except JobLookupError as e:
        print("Scheduler 오류 발생", e)
        return
    while True:
      try:
        print("Running main process............","| [time] ", str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec))
        time.sleep(5)  
      except KeyboardInterrupt:
        import sys
        print("Ctrl + C 중지, Job 제거 후 프로그램 종료")
        sched.remove_all_jobs()
        sys.exit()
  except KeyboardInterrupt:
    print("Ctrl + C 중지")
    
if __name__ == "__main__":
  main()