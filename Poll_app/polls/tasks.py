from celery import shared_task


@shared_task
def say_hi():
    return "HI!!!!!"
