import mysql.connector


def connect():
    mydb = mysql.connector.connect(host='localhost', port=3306, user='root', password='football', database='gym')
    return mydb
