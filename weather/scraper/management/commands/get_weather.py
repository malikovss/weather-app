import time
from django.utils.timezone import datetime
from django.core.management import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from scraper.scraper import scrape
from scraper.models import Weather


scheduler = BackgroundScheduler()

def save_data_on_db():
    try:
        day = datetime.now().day
        last_object_on_db = Weather.objects.latest('created_at')
        if last_object_on_db and last_object_on_db.created_at.day == day: return False
        data = scrape.get_weather()
        if not data: return
        for i in data:
            w = Weather(**i)
            w.save()
        print('data saved')
    except:
        pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        save_data_on_db()
        scheduler.add_job(save_data_on_db, 'interval', days=1)
        scheduler.start()
        try:
            while True:
                time.sleep(60)
        except (KeyboardInterrupt,SystemExit):
            scheduler.shutdown()