import os
import signal

from flask import Flask, request
from db_connector import *

app = Flask(__name__)


# supported methods

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
@app.route('/users/', defaults={'user_id': None})

def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        try:
            post_user = add_user(user_id, user_name )
            return {"user": post_user['name'], 'status': 'saved'}, 200 # status code
        except Exception :
            return {'reason': 'id already exists', 'status': 'error'}, 500  # status code

  # todo elif for get put and delete
    elif request.method == "PUT":
        request_data = request.json
        user_name = request_data.get('user_name')
        updadated_user = update_user(user_id,user_name)
        if updadated_user is None:
            return {'reason:': 'no such id', 'status': 'eror'}, 500  # status code
        return {'user_updated:': updadated_user['name'], 'status': 'ok'}, 200  # status code

    elif request.method=="DELETE":
        deleted = delete_user(user_id)
        if deleted is True:
            return {'status': 'saved', 'user id': user_id}, 200
        return {'reason:': 'no such id', 'status': 'eror'}, 500  # status code


    elif request.method=="GET":
        if user_id == None :
           users = selectAll_user()
           return users,  200 # status code
        user = select_user(user_id)
        if user is None :
            return {'status': 'error', 'reason': 'no such id'} ,500
        return user, 200 # status code

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
