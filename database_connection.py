import mysql.connector
from mysql.connector import Error, pooling, connect
from mysql.connector.errors import PoolError
from config import config
import random


class GetDBConnection:
    _mysql_pool = None

    def __init__(self):
        self.host = config["MYSQL_HOST"]
        self.user = config["MYSQL_USER"]
        self.pwd = config["MYSQL_PASSWORD"]
        self.db = config["MYSQL_DATABASE"]
        self.port = config["MYSQL_PORT"]
        self.pool_size = 2

    def connect(self):
        try:
            # _mysql_connection = connect(host=self.host,
            #                             port=self.port,
            #                             database=self.db,
            #                             user=self.user,
            #                             passwd=self.pwd,
            #                             auth_plugin="mysql_clear_password")

            _mysql_connection = connect(host="localhost",
                                        port=3306,
                                        database="app_db",
                                        user="root",
                                        passwd="root",
                                        auth_plugin="mysql_clear_password")

            return _mysql_connection
        except Error as e:
            print("Error while connecting to MySQL", e)
