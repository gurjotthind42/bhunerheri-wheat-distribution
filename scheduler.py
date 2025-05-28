from apscheduler.schedulers.background import BackgroundScheduler
from scraper import refresh_fps_data, update_yesterday_distributions

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_fps_data, 'interval', minutes=15)
    scheduler.add_job(update_yesterday_distributions, 'cron', hour=0, minute=0)
    scheduler.start()
