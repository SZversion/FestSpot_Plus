from typing import Optional
import mysql.connector
from mysql.connector import Error
from sqlmodel import Field, SQLModel
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


def user_info(userid: str):
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM user_tb WHERE userid = %s", (userid,))
            result = cur.fetchone()
        except Error as err:
            print("Error: ", err)
            result = False
    return result


def create_user(userid: str, password: str, email: str, nickname: str, img_url: str):
    with mysql.connector.connect(**config.MYSQL_DB_CONFIG) as conn:
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO user_tb VALUES (default, %s, %s, %s, %s, %s, default, default, default, default)",
                (
                    userid,
                    password,
                    email,
                    nickname,
                    img_url,
                ),
            )
            conn.commit()
            result = cur.lastrowid
            print(result)
        except Error as err:
            print("Error: ", err)
            result = False
    return result


class User(SQLModel, table=True):
    __tablename__ = "user_tb"

    id: Optional[int] = Field(default=None, primary_key=True)
    userid: str = Field(index=True)
    password: str
    email: str
    nickname: str
    img_url: str
