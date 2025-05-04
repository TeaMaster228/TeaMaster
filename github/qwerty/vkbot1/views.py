from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import vk
import random
import database

vk_api = vk.API(access_token='vk1.a.hITSlDpaKRNyRyVPYfa4q3cqgXrfm-qmtJIApR9TmHjFrjPucpOiuHmfs8ekUNuejcdox-yMihf59qxdzr9cC5z7Vmm1fAVpha4JmI7PxxEdS48bbox25TQoqMufSCa5_rvqko1-uBCZziRj3872d3DpZ2E1fCkY3ktYMINPD7D2heNm5PYfowZkdtwCfeh8D02bRC1Fy7e7-kLu7BQo_Q')

@csrf_exempt
def init(request):
    body = json.loads(request.body)
    if body["type"] == "confirmation":
        print("body")
        return HttpResponse ("91862c04")


def talk(request):
    body = json.loads(request.body)
    data = database.get_db()
    user_id = body["object"]["message"]["from_id"]
    if body ["object"]["message"]["text"].find('/') != -1:
        mes = body["object"]["message"]["text"].split('/')
        database.insert_db(mes[0],mes[1])
        vk_api.messages.send(user_id=user_id, message="I have recorded a new phrase", random_id=random.randint(1,500000000000000),v=5.199)
    else:
        w = False
        for i in data:
            if i[1] == body ["object"]["message"]["text"]:
                w = True
                messages = i[2]
                vk_api.messages.send(user_id=user_id, message=messages, random_id=random.randint(1,50000000000000),v=5.199)
        if  not w :
            message1 = "Я не понимаю это сообщение"
            message2 = "напиши мне пару Сообщение/Ответ, если ты хочешь добавить новую фразу. Не забудь разделить их знаком /"
            vk_api.messages.send(user_id=user_id, message=message1, random_id=random.randint(1,500000000000000),v=5.199)
            vk_api.messages.send(user_id=user_id, message=message2, random_id=random.randint(1,500000000000000),v=5.199)

@csrf_exempt

def get_message(request):
    body = json.loads(request.body)
    print(body)
    if body["type"] == 'message_new':
        if "payload" in body["object"]["message"]:
            if body["object"]["message"]["payload"] == '{"cammand":"start"}':
                start(request)
            else:
                user_id = body["object"]["message"]["from_id"]
                group = body["object"]["message"]["payload"]
                database.add_member(group,user_id)
        else:
            talk(request)
    return HttpResponse("ok")


def start(request):
    body = json.loads(request.body)
    user_id = body["object"]["message"]["from_id"]
    message = "Привет, чтобы получить от меня уведомление выбери свою группу из предложенных вариантов"
    keyboard = {
        "one_time": True,
        "buttons": [
            [{
                    "action": {
                        "type": "text",
                        "playload": '{"command":"friends"}',
                        "label": "Друзья"
                    },
                    "color": "primary"
                },
                {
                    "action": {
                        "type": "text",
                        "playload": '{"command":"classmates"}',
                        "label": "Одноклассники"
                    },
                    "color": "primary"
                },
                {
                  "action": {
                        "type": "text",
                        "playload": '{"command":"programmers"}',
                        "label": "Программисты"
                    },
                    "color": "primary"
                }
            ]        
        ]
    }
    vk_api.messages.send(user_id=user_id, message=message, keyboard=json.dumps(keyboard), ramdom_id=random.randint(1,500000000),v=1.199)




def admin(request):
    with open('vkbot1/templates/index2.html', 'r') as file:
        return HttpResponse(file.read())

def script(request):
    with open('vkbot1/templates/script.js','r') as file:
        return HttpResponse(file.read())
    
def client_server(request):
    body = json.loads(request.body)
    res = {}
    print('client')
    if body ["type"] == "login":
        print('login')
        if (body["username"] == "admin") and (body["password"] == "admin"):
            print('admin')
            res["correct"] = True
            res["val"]= database.get_groups()
            with open('myBotVK/templates/admin.html', 'r') as file:
                res["html"] = file.read()
        else:
            res["correct"] = False
            print(res)
        return HttpResponse(json.dumps(res))
    elif body["type"] == "postNewMessage":
        users_chat_id = database.get_member(body["group"])
        #print(users_chat_id)
        for i in users_chat_id:
            vk_api.messages.send(user_id=i, message=body['content'], random_id=random.randint(1,500000000000000),v=5.199)
        return HttpResponse(json.dumps({"res":"ok"}))

def get_group():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("CELECT group_name FROM groups")
    result = cursor.fetchall()
    conn.close()
    for i in range(0,len(result)):
        result[i] = result[i][0]
    return result


def client_server(request):
    body = json.loads(request.body)
    res = {}
    if body["type"] -- "login":
        if (body["username"] == "admin") and (body["password"] == "admin"):
            res["correct"] - True
            res["val"] = database.get_groups()
            with open('vkbot1/templates/admin.html', 'r') as file:
                res["html"] = file.read()
        else:
            res["correct"] = False
        #print(res)
        return HttpResponse(json.dumps(res))
    elif body["type"] == "postNewMessage":
        users_chat_id = database.get_member(body["group"])
        #print(users_chat_id)
        for i in users_chat_id:
            vk_api.messages.send(user_id=i, message=body['content'], random_id=random.randint(1,500000000000000000),v=5.199)
        return HttpResponse(json.dumps({"res":"ok"}))
    

