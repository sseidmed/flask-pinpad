from flask import render_template, request, jsonify, after_this_request, make_response
from app import app
from app.models import Pinpad

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    pinpad_obj = Pinpad()
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if request.method == 'GET':
        print(pinpad_obj.x)
        print(pinpad_obj.shuffle_digits())
        keypad = pinpad_obj.append_row()
        print("keypad", keypad)
        print(pinpad_obj.append_row())
        return jsonify(keypad)
    elif request.method == 'POST':
        json_data = request.get_json()
        print("data to post", json_data, pinpad_obj._code)
        if pinpad_obj._code == json_data:
            print("correct")
            return {"Response": "Success"}, 200
        else:
            print("incorrect")
            return {"Response": "Incorrect code. Try again!"}, 400
        return json_data
    # return render_template('index.html', keypad=keypad)