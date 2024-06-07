from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import random
import base64
import os

select1 = ['공부', '쉴래', '놀래', '배고파']
result_lst = []
app = Flask(__name__, static_folder='static/build', static_url_path='/')

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/endpoint', methods=['POST'])
def handle_data():
    global result_lst
    data = request.json
    selectedOption = data['selectedOption']
    if selectedOption in select1:
        result_lst = []
    result_lst.append(selectedOption)
    print(f"Received Option: {selectedOption}", result_lst)
    return jsonify({"status": "success", "receivedOption": selectedOption}), 200, result_lst

@app.route('/api/activity-create', methods=['POST'])
def create_activity():
    data = request.json
    selectedOption = data['selectedOption']
    print(f"Activity Created with Option: {selectedOption}")
    return {'message': 'Activity created successfully'}, 201

def get_result_from_first_db(number_of_people, location, type_of_food):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM '1시간 식사' WHERE 인원=? AND 위치=? AND 음식종류=?", (number_of_people, location, type_of_food))
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None



def get_result_from_second_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `30분~1시간 식사` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None

def get_result_from_third_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `우주공강 놀래`")
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None
def get_result_from_4th_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `1시간 놀래` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None
def get_result_from_5th_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `30분~1시간 놀래` ")
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None

def get_result_from_6th_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `30분~1시간 쉴래` ")
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None

def get_result_from_7th_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `1시간 쉴래(카페)` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None

def get_result_from_8th_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `30분~1시간 공부할래` ")
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None
    

def get_result_from_9th_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값, 사진 FROM `1시간 공부(카페)` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()

    if results:
        result = random.choice(results)
        결과값, 이미지 = result
        이미지_base64 = base64.b64encode(이미지).decode('utf-8')  # 이미지를 Base64로 인코딩하고 문자열로 디코딩
        return (결과값, 이미지_base64)
    else:
        return None


        
    
    

@app.route('/search', methods=['GET'])
def search():
    mode = request.args.get('mode')  # `mode` URL 파라미터를 사용하여 동작 모드 결정
    if mode == '1':
        number_of_people = int(request.args.get('number_of_people'))
        location = request.args.get('location')
        type_of_food = request.args.get('type_of_food')

        if not (number_of_people and location and type_of_food):
            return jsonify({'error': 'Missing data for number_of_people, location, or type_of_food'}), 400

        result = get_result_from_first_db(number_of_people, location, type_of_food)

        if result:
            result_value, image_base64 = result
            # 결과값과 Base64로 인코딩된 이미지를 JSON 형태로 클라이언트에 전송
            return jsonify({'result_value': result_value, 'image': image_base64})
        else:
            return jsonify({'error': 'No results found'}), 404


    elif mode == '2':

        location = request.args.get('location')

        if not (location):
            return jsonify({'error': 'Missing data for location'}), 400

        result = get_result_from_second_db(location)

        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    elif mode == '3':
        result = get_result_from_third_db()
        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404



    elif mode == '4':

        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        result = get_result_from_4th_db(location)

        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    elif mode == '5':
        result = get_result_from_5th_db()
        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    elif mode == '6':
        result = get_result_from_6th_db()
        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    elif mode == '7':
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        result = get_result_from_7th_db(location)

        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    elif mode == '8':
        result = get_result_from_8th_db()
        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    elif mode == '9':
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        result = get_result_from_9th_db(location)

        if result:
            결과값, 이미지_base64 = result
            return jsonify({'result': 결과값, 'image': 이미지_base64})
        else:
            return jsonify({'error': 'No results found'}), 404

    else:
        return jsonify({'error': 'Invalid or missing mode parameter'}), 400

    return jsonify({'result': result[0]}) if result else jsonify({'error': 'No results found'}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)