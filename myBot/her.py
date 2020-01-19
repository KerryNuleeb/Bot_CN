from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
import get_pictures
import goup_pictures

token = "71422acb612bfd91f6f2b3b12b63024d8772614a4a112ac23644853241b3b72350506ec2c47510193e785"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print("Текст сообщения: " + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response.find('привет') != -1:
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Даров, петушок!', 'random_id': 0})
                elif response.find('мемы') != -1:
                    attachment = get_pictures.get(vk_session, -95958948, session_api)
                    vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Я накакал', 'random_id': 0, "attachment": attachment })
