import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import my_token

vk_session = vk_api.VkApi(token=my_token)
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:

                msg = event.text.lower()
                id = event.chat_id

                if msg == 'hi':
                    sender(id, 'Hi!')

                if msg == 'how are you?':
                    sender(id, 'Good! Thank you!')

                if msg in ['some bad word']:
                    sender(id, 'It really offends me')

