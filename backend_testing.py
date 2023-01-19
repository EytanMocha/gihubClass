import pymysql
import requests
from pymysql.cursors import DictCursor

idOfTheUser = 1  # local id for post  test

res = requests.post(f'http://127.0.0.1:5000/users/{idOfTheUser}', json={"user_name": "john"})
print(res.json())


req = requests.get(f'http://127.0.0.1:5000/users/{idOfTheUser}')
print(f"Status Code: {req.status_code}, Content: {req.json()}")



schema_name = 'freedb_Eitan123123'
# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@', db=schema_name, cursorclass= DictCursor)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute(f"SELECT * FROM {schema_name}.users WHERE id = '{idOfTheUser}'")

user = cursor.fetchone()
print(user)
cursor.close()
conn.close()
