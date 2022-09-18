import requests

from django.conf import settings
from practice.celery import app

from apps.user.models import Visits


from django.core.mail import send_mail


@app.task
def send_message(email):

    send_mail(
    'Hello',
    'you are registred....',
    # settings.EMAIL_HOST_USER,
    'zarinakudajberdikyzy@gmail.com',
    [email],
    fail_silently=False,
    
)



@app.task
def send_message_to_tg():
    token='5444300359:AAENQiMZ9_AYTpFKSSMpJAuVJjY2g4Ygmes'
    url='https://api.telegram.org/bot5444300359:AAENQiMZ9_AYTpFKSSMpJAuVJjY2g4Ygmes/sendMessage?'
    channel_id='-1001607346884'
    text=' вчера было сделанно - {} запрсов общ кол-во {}'
    try:
        visit=Visits.objects.get(id=1)
        response=requests.post(url=url,data={'chat_id':channel_id,'text':text.format(visit.count,visit.all_count)})

    except Exception as ex:
            print(f'error : {ex}')







