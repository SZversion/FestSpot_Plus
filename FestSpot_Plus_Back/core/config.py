# config/config.py

PORT = 8080

HOST = "0.0.0.0"

APP = "app:app"

MYSQL_DB_CONFIG = {
    "host": "127.0.0.1",
    "database": "festspot_db",
    "user": "root",
    "password": "1q2w3e4r!",
    "pool_size": 10,
    "pool_name": "mysql_pool",
}

API_PREFIX = "/api"
