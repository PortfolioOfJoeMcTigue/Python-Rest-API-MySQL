import os
import pymysql

class DBConnection():

    def get_database_connection(self):
        db_config = self.configure_database()
        db_conn = pymysql.connect(**db_config)
        return db_conn
    
    def configure_database(self):
        HOST = os.getenv('HOST')
        DATABASE = os.getenv('DATABASE')
        USERNAME = os.getenv('USERNAME')
        PASSWORD = os.getenv('PASSWORD')

        db_config = {
            'host' : HOST,
            'database' : DATABASE,
            'user' : USERNAME,
            'password' : PASSWORD
        }
        return db_config;