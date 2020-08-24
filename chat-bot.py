import requests
url = 'https://api.telegram.org/bot<Api key>/'


def get_chat_id(result):
    chat_id = result['message']['chat']['id']
    return chat_id


def get_message_text(result):
    message_text = result['message']['text']
    return message_text

def get_last_update(req):
    response = requests.get(req + 'getUpdates')
    response = response.json()
    result = response['result']
    last_update_index = len(result) - 1
    return result[last_update_index]


def send_message(chat_id,text):
    params = {'chat_id':chat_id,'text':text}
    response = requests.post(url + 'sendMessage',params)
    return response

def bot_reply():
    update_id = get_last_update(url)['update_id']
    while True:
        update = get_last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == 'hi':
                send_message(get_chat_id(update), 'Hello ' + update['message']['chat']['first_name'])
            elif get_message_text(update).lower() == 'hello':
                send_message(get_chat_id(update), 'How can i help you')
            else:
                send_message(get_chat_id(update), 'i dont understand you')
            update_id +=1
            print(update_id)


bot_reply()




