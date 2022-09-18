import requests
import datetime
from django.utils import timezone
from apps.user.models import Visits 
from utils.conf_file import *



class VisitsMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        r= self.get_response(request)

        
        assert hasattr(request, 'user')
        # if request.user.is_authenticated:
        try:
            if request.method:
                today=datetime.date.today()
                visit = Visits.objects.get(id=1)

                if visit.day==today:
                    visit.count +=1
                    visit.all_count+=visit.count
                    visit.day=timezone.now()
                    visit.save()
                else:
                    # response=requests.post(url=url,data={'chat_id':channel_id,'text':text.format(visit.count,visit.day,visit.all_count)})
                    visit.all_count+=visit.count
                    visit.day=timezone.now()
                    visit.count =0
                    visit.save()



        except Exception as ex:
            print(f'error : {ex}')
    
        return r

