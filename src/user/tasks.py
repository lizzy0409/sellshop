import datetime

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from celery import shared_task
from user.models import Profile
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from product.models import Product


@shared_task()
def send_mails():
    time_thresold = datetime.datetime.now() - datetime.timedelta(days=30)
    subject = "En cox sevilen 5 mehsulumuzu size teqdim edirik"

    user_emails = Profile.objects.filter(last_login_time__lte=time_thresold).values_list('email', flat=True)
    famous_products = Product.objects.filter(total_rating__gte=4)[:4]

    for user_email in user_emails:
        html_content = render_to_string("email_template.html", {"title": subject, 'famous_products': famous_products})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(subject, text_content, 'saturnchm@gmail.com', user_email)
        email.attach_alternative(html_content, "text/html")
        email.send()

    # send_mail(subject=subject, message=message, from_email='saturnchm@gmail.com',
    #           recipient_list=['aytacaliyeva133@gmail.com'], fail_silently=False)
