import requests

from utils.conf_file import *

class Telegram:
    def __init__(self,get_response):
        self.get_response=get_response
    

    def __call__(self,request):
        respon= self.get_response(request)
        return respon

    
    def send_message(self,request):
        try:
            print(request.user.is_authenticated)
            assert hasattr(request, 'user')
            if request.user.is_authenticated:
                username=request.user.username
                method=request.method
            else:
                username='неизвестный'
            response=requests.post(url=url,data={'chat_id':channel_id,'text':text.format(username,method)})

        except Exception as ex:
            print(f'error : {ex}')
    
        # return respon


# def send_telegram(text: str) -> response:
#     try:
#         token = "1917622909:AAHmC_iVcl6Az_f6JrDwL3ZXOo4nWnDbdAU"
#         url = "https://api.telegram.org/bot"
#         channel_id = "-1001445976600"
#         url += token
#         method = url + "/sendMessage"
#         r = requests.post(method, data={
#             "chat_id": channel_id,
#             "text": text
#         })
#         print('done')
#         if r.status_code == '200':
#             return 'eeee'
#         else:
#             return r.status_code
#     except Exception as ex:
#         print(ex)


# if name == 'main':
#     print(send_telegram("hello world!"))