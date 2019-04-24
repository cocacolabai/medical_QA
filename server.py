from websocket_server import WebsocketServer
from find_anwser import FindAnwser
import json
import requests

def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "58a614b618684bc8b4967221b70c867d"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "225240"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result["text"]

anwser_finder = FindAnwser()
# Called for every client connecting (after handshake)
def new_client(client, server):
        print("New client connected and was given id %d" % client['id'])
        #server.send_message_to_all("a new client...")
        server.send_message(client,"我是小旭，您最贴心的导诊机器人，请问有什么可以帮到您？")


# Called for every client disconnecting
def client_left(client, server):
        print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    global anwser_finder
    if len(message) > 200:
            message = message[:200]+'..'
    print("Client(%d)_address%s said: %s" % (client['id'],client['address'], message))
    #server.send_message(client,'用户编号'+str(client['id'])+':'+message)
    anwser = str(anwser_finder.anwser(message))
    if anwser == "":
        anwser = auto_reply(message)
    server.send_message(client,"小旭："+anwser)

PORT=9001
server = WebsocketServer(PORT, host="192.168.177.130")
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
