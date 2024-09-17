from flask import jsonify

from utilities import DBConnection as dbconn

class UserService():

    mydb = dbconn.DBConnection()
    myconn = mydb.get_database_connection()
    mycursor = myconn.cursor()

    def add_user_to_repository(self, data):
        user_name = data.get('user_name')
        email_address = data.get('email_address')
        password = data.get('password')
        sql_request = "INSERT INTO users (user_name, email_address, password) VALUES (%s, %s, %s)"
        tup = (user_name, email_address, password)
        try:
            self.mycursor.execute(sql_request, tup)
            self.mycursor.connection.commit()
            return jsonify({'message': 'New User was successfully entered into database'})
        except Exception as e:
            return jsonify({'error': str(e)})