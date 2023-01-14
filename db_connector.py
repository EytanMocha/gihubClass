import datetime
import pymysql
from pymysql.cursors import DictCursor


def add_user(user_id, username):
    schema_name = 'freedb_Eitan123123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@', db=schema_name,cursorclass= DictCursor)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    creation_date = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (name, id, creation_date) VALUES ('{username}', {user_id},'{creation_date}')")

    count = cursor.rowcount
    cursor.close()
    conn.close()
    if count > 0:
        return select_user(user_id)
    return None

def update_user(user_id, username):
    schema_name = 'freedb_Eitan123123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@', db=schema_name,cursorclass= DictCursor)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    cursor.execute(f"UPDATE {schema_name}.users SET name = '{username}' WHERE id ='{user_id}'")
    count = cursor.rowcount
    cursor.close()
    conn.close()
    if count > 0:
        return select_user(user_id)
    return None


def delete_user(user_id):
    schema_name = 'freedb_Eitan123123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE id = '{user_id}'")
    count = cursor.rowcount

    cursor.close()
    conn.close()
    return count > 0

def selectAll_user():
    schema_name = 'freedb_Eitan123123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@', db=schema_name, cursorclass= DictCursor)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {schema_name}.users ")
    users = cursor.fetchall()

    cursor.close()
    conn.close()
    return users
def select_user(user_id):
    schema_name = 'freedb_Eitan123123'
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@', db=schema_name, cursorclass= DictCursor)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"SELECT * FROM {schema_name}.users WHERE id = '{user_id}'")

    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user