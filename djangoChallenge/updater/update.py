
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from updater import requestsUpdater

def schedule_request(request, request_body_post, date_and_time):
    scheduler = BackgroundScheduler()
    if request == 'POST':
        request_body = request_body_post
    else :
        request_body = '{}'
    scheduler.add_job(requestsUpdater.send_request, 'date', run_date=date_and_time, args=(request, request_body))
    scheduler.start()