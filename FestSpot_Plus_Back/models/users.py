import mysql.connector
from mysql.connector import Error
from core import config


def list_user():
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM user_tb")
            results = cur.fetchall()
        except Error as err:
            print("Error: ", err)
            results = False
    return results
