from flask import jsonify

from utilities import DBConnection as dbconn

class ExamInfoService():

    mydb = dbconn.DBConnection()
    myconn = mydb.get_database_connection()
    mycursor = myconn.cursor()

    # def __init__(self):
    #     self.conn = self.dbconn.DBConnection()
    #     self.cursor = self.conn.get_database_connection()

    def add_exam_information_to_repository(self, data):
        exam_name = data.get('exam_name')
        exam_cost = data.get('exam_cost')
        pass_percentage = data.get('pass_percentage')
        info_address = data.get('info_address')
        active = data.get('active')
        subcategory = data.get('subcategory')
        category = data.get('category')
        goto_page = data.get('goto_page')
        bg_color = data.get('bg_color')

        sql_request = "INSERT INTO test_information (exam_name, exam_cost, pass_percentage, info_address, active, subcategory, category, goto_page, bg_color) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        tup = (exam_name, exam_cost, pass_percentage, info_address, active, subcategory, category, goto_page, bg_color)
        try:
            self.mycursor.execute(sql_request, tup)
            self.mycursor.connection.commit()
            return jsonify({'message': 'New test info was successfully entered into database'})
        except Exception as e:
            return jsonify({'error': str(e)})
    
    def get_list_of_exams_by_category_from_repository(self, data):
        category = data.get('category')
        sql_request = "SELECT id, exam_name, exam_cost, pass_percentage, info_address, category, subcategory, active FROM test_information WHERE category='{}'"
        sql_request = sql_request.format(category)
        try:
            self.mycursor.execute(sql_request)
            results = [{'id': id, 'exam_name': exam_name, 'exam_cost': exam_cost, 'pass_percentage': pass_percentage, 
                        'info_address': info_address, 'category': category, 'subcategory': subcategory, 'active': active} 
                        for id, exam_name, exam_cost, pass_percentage, info_address, category, subcategory, active in self.mycursor.fetchall()]
            return jsonify(results)
        except Exception as e:
            return jsonify({'error': str(e)})
        
    def get_list_of_exams_by_category_and_subcategory_from_repository(self, data):
        category = data.get('category')
        subcategory = data.get('subcategory')
        sql_request = "SELECT category, subcategory, goto_page, exam_name FROM test_information WHERE active=1 AND category='{}' AND subcategory='{}'"
        sql_request = sql_request.format(category, subcategory)
        try:
            self.mycursor.execute(sql_request)
            results = [{'category': category, 'subcategory': subcategory, 'goto_page': goto_page, 'exam_name': exam_name} 
                       for category, subcategory, goto_page, exam_name in self.mycursor.fetchall()]
            return jsonify(results)
        except Exception as e:
            return jsonify({'error': str(e)})
        
    def get_distinct_list_of_active_exam_categories_from_repository(self):
        sql_request = "SELECT Distinct category FROM test_information WHERE active=1"
        try:
            self.mycursor.execute(sql_request)
            results = [{'category': category} for category in self.mycursor.fetchall()]
            return jsonify(results)
        except Exception as e:
            return jsonify({'error': str(e)})
        
    def get_list_of_all_active_exams_from_repository(self):
        sql_request = "SELECT exam_name, exam_cost, pass_percentage, info_address, subcategory, category, goto_page FROM test_information WHERE active=1"
        try:
            self.mycursor.execute(sql_request)
            results = [{'exam_name': exam_name, 'exam_cost': exam_cost, 'pass_percentage': pass_percentage, 
                        'info_address': info_address, 'subcategory': subcategory,'category': category, 'goto_page': goto_page } 
                        for exam_name, exam_cost, pass_percentage, info_address, subcategory, category, goto_page in self.mycursor.fetchall()]
            return jsonify(results)
        except Exception as e:
            return jsonify({'error': str(e)})
        
    