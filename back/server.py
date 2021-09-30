from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

packets = [{"id": 1,
              "name": "item1",
              "sizex": 100.,
              "sizey": 100.,
              "sizez": 100.,
              "weight": 100.}, 
            {"id": 2,
              "name": "item2",
              "sizex": 101.,
              "sizey": 100.,
              "sizez": 110.,
              "weight": 101.}]
nextId = 0
for i in packets:
    nextId = max(i["id"], nextId)

@app.route('/data', methods=['GET'])
def sendData():
    response = {}
    response['data'] = packets
    response['nextId'] = nextId
    return jsonify(response)

@app.route('/data', methods=['POST'])
def postData():
    post_data = request.get_json()
    newPacket = {
        "id": int(post_data.get("id")),
        "name": post_data.get("name"),
        "sizex": float(post_data.get("sizex")),
        "sizey": float(post_data.get("sizey")),
        "sizez": float(post_data.get("sizez")),
        "weight": post_data.get("weight")
    }
    packets.append(newPacket)
    global  nextId
    nextId = max(nextId, newPacket["id"]) + 1
    return jsonify({"result" : "success"})

@app.route('/data/<idd>', methods=['PUT'])
def putData(idd):
    print(idd)
    idd = int(idd)
    post_data = request.get_json()
    editedPacket = {
        "id": int(post_data.get("id")),
        "name": post_data.get("name"),
        "sizex": float(post_data.get("sizex")),
        "sizey": float(post_data.get("sizey")),
        "sizez": float(post_data.get("sizez")),
        "weight": post_data.get("weight")
    }
    for i in range(len(packets)):
        if packets[i]["id"] == idd:
            packets[i] = editedPacket
    return jsonify({"result" : "success"})

@app.route('/data/<idd>', methods=['DELETE'])
def deleteData(idd):
    idd = int(idd)
    for row in packets:
        if row["id"] == idd:
            packets.remove(row)
    return jsonify({"result" : "success"})


if __name__ == '__main__':
    app.run(debug=True)

