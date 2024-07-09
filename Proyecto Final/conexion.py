from beautifultable import BeautifulTable
import mysql.connector
from datetime import datetime

class Conexion:
    def __init__(self):
        self.__connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bdd_kill",
            port="3306"
        )
        self.__cursor = self.__connection.cursor()

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor
