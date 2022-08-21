from flask import Flask, request, jsonify
import const 
import requests

app = Flask(__name__)

print("Chat Server is ready...")

count = 0

@app.route('/chat',methods=['POST'])
def createEmp():
    global count
    count +=1
    
    data = {
    'dest':request.json['dest'],
    'name':request.json['name'],
    'msg':request.json['msg'],
    'id':request.json['id'],
    'count':count,
    }
    ip = const.registry[request.json['dest']][0]
    port = const.registry[request.json['dest']][1]

    print(str(count) + " - RESPONSE: " + request.json['msg'] + " - FROM: " +  request.json['name'] + " - TO: " +  request.json['dest'] + '\n')
    response = requests.post(ip+":"+str(port)+'/chat', json = data) #2
    return "ACK"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)