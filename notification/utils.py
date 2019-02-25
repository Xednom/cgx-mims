from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

sender = getattr(settings, "EMAIL_SENDER", "support@tgx.com")


def send_email(subject, receiver, html_content):
    text_content = 'This is an important message.'
    email = EmailMultiAlternatives(
        subject,
        text_content,
        sender,
        [receiver]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def send_sample_email():
    subject = 'Sample email'
    html_template = get_template('sample-email.html')
    context = {

    }
    html = html_template.render(context)
    send_email(
        subject,
        'test@test.com',
        html,
    )
