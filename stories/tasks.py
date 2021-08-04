from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from stories.models import Subscriber, Recipe
from django.db.models import Count
from django.conf import settings

@shared_task
def send_mail_subscribers():
    user_emails = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    recipes = Recipe.objects.annotate(Count('comment__context')).order_by('-comment__context__count')[:3]
    subject = ('Latest popular recipes for you')
    context = {
        'recipes': recipes,
        'SITE_ADDRESS': settings.SITE_ADDRESS
    }
    body = render_to_string('emails/email-subscribers.html', context)

    mail = EmailMessage(subject, to= user_emails, from_email=settings.EMAIL_HOST_USER, body=body)
    mail.content_subtype='html'
    mail.send()