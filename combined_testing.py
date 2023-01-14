import pymysql
import requests
from pymysql.cursors import DictCursor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    user_id = 1
    res = requests.post(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name":"john"})

    print(res.json())

    req = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
    print(f"Status Code: {req.status_code}, Content: {req.json()}")


    def select_user(user_i):
        schema_name = 'freedb_Eitan123123'
        # Establishing a connection to DB
        conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_eitan123', passwd='kF!%6FMFtgg@m!@',db=schema_name, cursorclass=DictCursor)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Inserting data into table
        cursor.execute(f"SELECT * FROM {schema_name}.users WHERE id = '{user_i}'")

        user = cursor.fetchone()

        cursor.close()
        conn.close()
        return user
    print("______________________________")
    print(select_user(user_id))

    driver = webdriver.Chrome(service=Service("C:\\Users\IBI-LAP\Downloads\chromedriver_win32\chromedriver"))
    driver.get(f"http://127.0.0.1:5001/users/get_user_data/{user_id}")
    print(driver.title)
    tag_name = driver.find_element(By.ID, "user")
    print(tag_name.accessible_name)
except Exception :
    print("test faild")