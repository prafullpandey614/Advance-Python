# '''
# install following modules

# pip install celery==4.4.3

# pip install redis==3.5.3
# '''

from celery import Celery

# Redis broker URL
BROKER_URL = 'redis://localhost:6379/0'


# We are creating an instance of Celery class by passing module name as Restaurant and broker as Redis.
celery_app = Celery('Restaurent',broker=BROKER_URL)

# we are decorating cooking_task function with @celery_app.task decorator.
# Functions which are decorated with @celery_app.task considered celery tasks.
@celery_app.task
def cooking_task(table_no,dishes):
    print("Start Cooking For Table Number : {}".format(table_no))
    for dish in dishes:
        print("Cooking : " + dish)
    print("Done Cooking For Table Number : {}".format(table_no))