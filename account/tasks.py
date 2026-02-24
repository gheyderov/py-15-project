from core.models import Subscribe
from product.models import Product
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


email_list = Subscribe.objects.values_list('email', flat=True)
products = Product.objects.all()[:3]


@shared_task
def email_to_subscribers():
    subject = 'Latest Products'
    message = render_to_string('email_to_subscribers.html', {
        'products' : products
    })
    mail = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=email_list
    )
    mail.content_subtype = 'HTML'
    mail.send()

