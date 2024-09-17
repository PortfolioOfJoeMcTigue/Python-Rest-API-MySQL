from flask import jsonify

from utilities import DBConnection as dbconn

class Questions():

    mydb = dbconn.DBConnection()
    myconn = mydb.get_database_connection()
    mycursor = myconn.cursor()

    def add_question_to_repository(self, data):
        id = data.get('id')
        exam_name = data.get('exam_name')
        question_number = data.get('question_number')
        question = data.get('question')
        scenario = data.get('scenario')
        choice_1 = data.get('choice_1')
        choice_2 = data.get('choice_1')
        choice_3 = data.get('choice_1')
        choice_4 = data.get('choice_1')
        choice_5 = data.get('choice_1')
        answer = data.get('answer')
        why = data.get('why')
        sql_request = "INSERT INTO questions (id, exam_name, question_number, question, scenario, choice_1, choice_2, choice_3, choice_4, choice_5, answer, why) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        tup = (id, exam_name, question_number, question, scenario, choice_1, choice_2, choice_3, choice_4, choice_5, answer, why)
        try:
            self.mycursor.execute(sql_request, tup)
            self.mycursor.connection.commit()
            return jsonify({'message': 'New question successfully entered into database'})
        except Exception as e:
            return jsonify({'error': str(e)})
        
    def get_question_details_by_exam_name_and_question_number_from_repository(self, data):
        exam_name = data.get('exam_name')
        question_number = data.get('question_number')
        sql_request = 'SELECT question_number, question, scenario, choice_1, choice_2, choice_3, choice_4, choice_5 FROM questions WHERE exam_name like \'%{}%\' AND question_number={}'
        sql_request = sql_request.format(exam_name, question_number)
        try:
            self.mycursor.execute(sql_request)
            result = [{'question_number': question_number, 'question': question, 'scenario': scenario, 
                       'choice_1': choice_1, 'choice_2': choice_2, 'choice_3': choice_3, 'choice_4': choice_4, 'choice_5': choice_5} 
                       for question_number, question, scenario, choice_1, choice_2, choice_3, choice_4, choice_5 in self.mycursor.fetchall()]
            return jsonify(result)
        except Exception as e:
            return jsonify({'error' : str(e)})
        
    def get_number_of_questions_by_exam_name_from_repository(self, data):
        exam_name = data.get('exam_name')
        sql_request = 'SELECT COUNT(*) AS number_of_questions FROM questions WHERE exam_name like \'%{}%\''
        sql_request = sql_request.format(exam_name)
        try:
            self.mycursor.execute(sql_request)
            number_of_questions = self.mycursor.fetchone()[0]
            result = {'number_of_questions': number_of_questions}
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)})