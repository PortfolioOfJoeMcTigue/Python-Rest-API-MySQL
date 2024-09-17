from flask import Flask, request, jsonify

from services import QuestionService as question_serv
from services import UserService as user_serv
from services import ExamInfoService as exam_serv

app = Flask(__name__)

@app.route('/exam', methods=['GET'])
def health_check():
    return jsonify({'Health_Check': 'Health Check Successful!'})

@app.route('/exam/question/add', methods=['POST'])
def add_question():
    data = request.get_json()
    q = question_serv.Questions()
    return q.add_question_to_repository(data)
            
@app.route('/exam/user_info/add', methods=['POST'])
def user_info_add():
    data = request.get_json()
    u = user_serv.UserService()
    return u.add_user_to_repository(data)
    
@app.route('/exam/testinformation/add', methods=['POST'])
def test_info_add():
    data = request.get_json()
    e = exam_serv.ExamInfoService()
    return e.add_exam_information_to_repository(data)

@app.route('/exam/byactivecategory/list', methods=['GET', 'POST'])
def get_list_of_exams_by_category():
    data = request.get_json()
    e = exam_serv.ExamInfoService()
    return e.get_list_of_exams_by_category_from_repository(data)
    
@app.route('/exam/bycategoryandsubcategory', methods=['GET', 'POST'])
def get_list_of_exams_by_category_and_subcategory():
    data = request.get_json()
    e = exam_serv.ExamInfoService()
    return e.get_list_of_exams_by_category_and_subcategory_from_repository(data)
    
@app.route('/exam/list/distinctactivecategories', methods=['GET'])
def get_list_of_active_exams_by_categories():
    e = exam_serv.ExamInfoService()
    return e.get_distinct_list_of_active_exam_categories_from_repository()
    
@app.route('/exam/list/allactiveinfo', methods=['GET'])
def get_list_of_all_tests():
    e = exam_serv.ExamInfoService()
    return e.get_list_of_all_active_exams_from_repository()

@app.route('/exam/question', methods=['GET', 'POST'])
def get_question():
    data = request.get_json()
    q = question_serv.Questions()
    return q.get_question_details_by_exam_name_and_question_number_from_repository(data)
    
@app.route('/exam/question/amount', methods=['GET', 'POST'])
def get_question_amount():
    data = request.get_json()
    q = question_serv.Questions()
    return q.get_number_of_questions_by_exam_name_from_repository(data)

if __name__ == "__main__":
    app.run(debug=True)

