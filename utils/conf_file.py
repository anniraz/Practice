token='5444300359:AAENQiMZ9_AYTpFKSSMpJAuVJjY2g4Ygmes'
url='https://api.telegram.org/bot5444300359:AAENQiMZ9_AYTpFKSSMpJAuVJjY2g4Ygmes/sendMessage?'
channel_id='-1001607346884'
text='пользователь  {} сделал  {} запрос'

# https://api.telegram.org/bot5444300359:AAENQiMZ9_AYTpFKSSMpJAuVJjY2g4Ygmes/sendMessage?chat_id=-1001607346884&text=hello
# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 








# from urllib import response
# import requests


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