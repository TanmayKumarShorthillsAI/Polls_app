from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Choice
from django.db.models.signals import post_save

@receiver(post_save, sender=Choice, dispatch_uid = "send_choice_email")
def send_choice_email(sender, instance, created, **kwargs):
    print(instance, created)
    if instance or created:
        send_mail(
            "Greetings!!",
            f"Thanks for participating in the poll \n Poll info: \n Question: {instance.question.question_text}\n Choice: {instance.choice_text}",
            "admin@django.com",
            ["tanmayk2001@gmail.com"],
            fail_silently=False
            
        )