from flask import Flask, request, Response
from flask_cors import CORS
from src import SERVER, MAIL, DINGDING

app = Flask(__name__)

CORS(app, resources=r'/*')


@app.route('/login', methods=['POST'])
def login():
    if request.json['name'] and request.json['A_id']:
        data = request.json
        return SERVER.login(data)
    else:
        return {'message': '输入参数错误'}


@app.route('/update_user_data', methods=['POST'])
def update_user_data():
    data = request.json
    SERVER.update_user_data(data)
    return Response("ok")


@app.route("/get_teacher", methods=["GET"])
def get_teacher():
    return SERVER.get_teacher()


@app.route("/get_reserve", methods=["GET"])
def get_reserve():
    teacher = request.args.get('teacher')
    return SERVER.get_reserve(teacher)


@app.route("/my_get_reserve", methods=["GET"])
def my_get_reserve():
    name = request.args.get('name')
    A_id = request.args.get('A_id')
    return SERVER.my_get_reserve(name, A_id)


@app.route("/my_get_data", methods=["GET"])
def my_get_data():
    name = request.args.get('name')
    return SERVER.my_get_data(name)


@app.route("/insert", methods=["POST"])
def insert():
    data = request.json
    SERVER.insert(data)
    MAIL.mailto(data)
    DINGDING.push("预约信息", data)
    return Response("ok")


@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    SERVER.delete(data)
    DINGDING.push("预约取消信息", data)
    return Response("ok")


@app.route("/export", methods=["POST", "GET"])
def export():
    return SERVER.export()


@app.route("/a_login", methods=["POST"])
def a_login():
    data = request.json
    return SERVER.a_login(data)


@app.route("/a_get_reserve", methods=["GET"])
def a_get_reserve():
    return SERVER.a_get_reserve()


@app.route("/rest_day", methods=["GET"])
def rest_day():
    return SERVER.rest_day()


@app.route("/setting_rest", methods=['POST'])
def setting_rest():
    data = request.json
    SERVER.setting_rest(data)
    return Response('ok')


@app.route("/del_rest", methods=['POST'])
def del_rest():
    data = request.json
    SERVER.del_rest(data)
    return Response('ok')


@app.route("/update_teacher", methods=['POST'])
def update_teacher():
    data = request.json
    return Response("OK")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
