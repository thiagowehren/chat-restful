from flask import Flask, request, jsonify
import sys
import const 
import requests
import threading
# Handle interactive loop

app = Flask(__name__)

@app.route('/chat',methods=['POST'])
def createEmp():

    data = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    }
    
    if(request.json['id'] == ''):
        print(str(request.json['count']) + " - MSG: " + request.json['msg'] + " - FROM: " +  request.json['name']) 
    else:
        print("TO: " + request.json['id'] +" - MSG: " + request.json['msg'] + " - FROM: " +  request.json['name']) 
    return "ACK"

me = str(sys.argv[1]) 

def sending():
    while True:
        dest = ''
        idmsg = ''
        replyQuestion = input("Reply (y or n): \n")

        if (str(replyQuestion).lower == 'y'):
            idmsg = input("MSG ID: \n")
        dest = input("TO: \n")
        msg = input("MSG: \n")

        data = {
            'dest':dest,
            'name':me,
            'msg':msg,
            'ip':const.registry[me][0],
            'id':idmsg,
        }

        reply = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/chat', json = data) #2
        if reply.text != "ACK":
            print("Error: Destination client did not receive message properly")
        else:
            pass

def receiving():
    app.run(host="0.0.0.0",port=const.registry[me][1])

if __name__ == '__main__':
    
    send = threading.Thread(target=sending)
    send.start()
    
    receive = threading.Thread(target=receiving)
    receive.start()