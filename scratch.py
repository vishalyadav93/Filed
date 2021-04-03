from flask import Flask, request, jsonify
from Factory import FactoryClass as f
import DatabaseConnect as DB_connect
from flask import Blueprint, jsonify
import inspect

app = Flask(__name__)



@app.route('/get/<path:path>', endpoint='get', methods=['GET'])
def select(path):
    try:
        audioFileType = list(filter(None, path.split('/')))
        #print(audioFileType)
        data = DB_connect.get_utility(*audioFileType)
        return data
    except Exception as e:
        return get500()

@app.route('/delete/<path:path>', endpoint='delete', methods=['DELETE'])
def delete(path):
    try:
        audioFileType = list(filter(None, path.split('/')))
        DB_connect.delete_utility(*audioFileType)
        return get200()
    except:
        return get500()

@app.route('/update/<path:path>', endpoint='update', methods=['PUT'])
def update(path):
    try:
        audioFileType = list(filter(None, path.split('/')))
        audioFileType.append(request.json['audioFileMetadata'])
        print(audioFileType)
        DB_connect.update_utility(*audioFileType)
        return get200()
    except Exception as e:
        print(e)
        return get500()

def get200():
    return jsonify({"status": "success"}), 200


@app.route('/create', methods=['POST'])
def create():
    try:
        content = request.json
        print('*'*20)
        print("in create",content)
        print('*' * 20)
        audioFileType = content['audioFileType']
        audioFileMetadata = content['audioFileMetadata']
        x=validate(audioFileType,audioFileMetadata)
        if(x!=None):
            return jsonify(x),400
        obj = f.create_object(audioFileType, audioFileMetadata)
        DB_connect.create_utility(obj)
        return jsonify({"status": "Success"}),200
    except Exception as e:
        return get500()


def get500():
    return jsonify({"status": "Internal Server Error"}), 500


def validate(type,payload):
    x=f.getClass(type)
    attributes = inspect.getmembers(x, lambda a: not (inspect.isroutine(a)))
    att=[a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
    exclude=['id','_sa_class_manager']

    for item in att:
        if  item[0] not in exclude:
            if(item[0] not in payload.keys()):
                return get400(item)
    return None


def get400(item):
    return {"status": "Bad Request", "Required": item[0]}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=False)
