import mysql.connector
from mysql.connector import Error
from datetime import datetime

def insertUser(title, src, celsius, des, high, low, updated):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='tuan123',
            database='weatherdb'
        )
        if conn.is_connected():
            sql = 'insert into weather(title, src, celsius, des, high, low, updated, createdat) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor = conn.cursor()
            createdat = datetime.today().strftime('%Y-%m-%d')
            cursor.execute(sql, (title, src, celsius, des, high, low, updated, createdat))
            conn.commit()
            return True
    except Error as e:
        print("loi let noi", e)
        return False

def checkExists():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='tuan123',
            database='weatherdb'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            createdat = datetime.today().strftime('%Y-%m-%d')
            sql2 = "SELECT * FROM weather WHERE createdat = '"+createdat+"'"
            cursor.execute(sql2)
            d = cursor.fetchall()
            if len(d) > 0:
                return False
            else:
                return True
    except Error as e:
        print("loi let noi", e)
        return False

def getDay(d):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='tuan123',
            database='weatherdb'
        )
        if conn.is_connected():
            cursor = conn.cursor()
            sql2 = "SELECT * FROM weather WHERE createdat = '"+d+"'"
            cursor.execute(sql2)
            d = cursor.fetchall()
            if len(d) > 0:
                return d
            else:
                return False
    except Error as e:
        print("loi let noi", e)
        return False