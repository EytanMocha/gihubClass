from flask import Flask

from db_connector import select_user

app = Flask(__name__)

@app.route("/users/get_user_data/<user_id>")
def get_user(user_id):
    user = select_user(user_id)
    if user == None:
        return f"<H1 id='error'> no such user:  {user_id} </H1>"
    return "<H1 id='user'>" + user['name'] + "</H1>"

# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)