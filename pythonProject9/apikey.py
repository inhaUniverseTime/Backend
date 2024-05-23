from flask import Flask, request, jsonify
import sqlite3
import random
import uuid

app = Flask(__name__)

api_keys = {}

@app.route('/generate_api_key', methods=['POST'])
def generate_api_key():
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({'error': 'Missing user_id'}), 400
    api_key = str(uuid.uuid4())
    api_keys[api_key] = user_id
    return jsonify({'api_key': api_key}), 201

@app.before_request
def verify_api_key():
    if request.path == '/generate_api_key':
        return
    api_key = request.headers.get('X-API-KEY')
    if not api_key or api_key not in api_keys:
        return jsonify({'error': 'Invalid or missing API key'}), 401

@app.route('/list_api_keys', methods=['GET'])
def list_api_keys():
    return jsonify(api_keys)

def execute_db_query(query, params=()):
    db_path = r"C:\Users\ins55\OneDrive\바탕 화면\database.db"
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute(query, params)
        results = c.fetchall()
    return random.choice(results) if results else None
def get_result_from_first_db(number_of_people, location, type_of_food):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM '1시간 식사' WHERE 인원=? AND 위치=? AND 음식종류=?", (number_of_people, location, type_of_food))
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_second_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `30분~1시간 식사` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_third_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `우주공강 놀래` ")
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_4th_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `1시간 놀래` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_5th_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `30분~1시간 놀래` ")
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_6th_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `30분~1시간 쉴래` ")
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_7th_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `1시간 쉴래(카페)` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_8th_db():
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `30분~1시간 공부할래` ")
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

def get_result_from_9th_db(location):
    conn = sqlite3.connect(r"C:\Users\ins55\OneDrive\바탕 화면\database.db")
    c = conn.cursor()
    c.execute("SELECT 결과값 FROM `1시간 공부(카페)` WHERE 위치=?", (location,))
    results = c.fetchall()
    conn.close()
    return random.choice(results) if results else None

@app.route('/search', methods=['GET'])
def search():
    mode = request.args.get('mode')
    if mode not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return jsonify({'error': 'Invalid or missing mode parameter'}), 400

    location = request.args.get('location')
    number_of_people = request.args.get('number_of_people')
    type_of_food = request.args.get('type_of_food')

    query = ""
    params = ()

    if mode == '1':
        number_of_people = int(request.args.get('number_of_people'))
        location = request.args.get('location')
        type_of_food = request.args.get('type_of_food')
        if not (number_of_people and location and type_of_food):
            return jsonify({'error': 'Missing data for number_of_people, location, or type_of_food'}), 400
        query = "SELECT 결과값 FROM '1시간 식사' WHERE 인원=? AND 위치=? AND 음식종류=?"
        params = (number_of_people, location, type_of_food)
        result = get_result_from_first_db(number_of_people, location, type_of_food)
    elif mode == '2':
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        query = "SELECT 결과값 FROM `30분~1시간 식사` WHERE 위치=?"
        params = (location,)
        result = get_result_from_second_db(location)

    elif mode == '3':
        query = "SELECT 결과값 FROM `우주공강 놀래`"
        result = get_result_from_third_db()
        return jsonify({'result': result[0]}) if result else jsonify({'error': 'No results found'}), 404

    elif mode == '4':
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        query = "SELECT 결과값 FROM `1시간 놀래` WHERE 위치=?"
        params = (location,)
        result = get_result_from_4th_db(location)

    elif mode == '5':
        query = "SELECT 결과값 FROM `30분~1시간 놀래`"
        result = get_result_from_5th_db()
        return jsonify({'result': result[0]}) if result else jsonify({'error': 'No results found'}), 404

    elif mode == '6':
        query = "SELECT 결과값 FROM `30분~1시간 쉴래`"
        result = get_result_from_6th_db()
        return jsonify({'result': result[0]}) if result else jsonify({'error': 'No results found'}), 404

    elif mode == '7':
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        query = "SELECT 결과값 FROM `1시간 쉴래(카페)` WHERE 위치=?"
        params = (location,)
        result = get_result_from_7th_db(location)

    elif mode == '8':
        query = "SELECT 결과값 FROM `30분~1시간 공부할래`"
        result = get_result_from_8th_db()
        return jsonify({'result': result[0]}) if result else jsonify({'error': 'No results found'}), 404

    elif mode == '9':
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Missing data for location'}), 400
        query = "SELECT 결과값 FROM `1시간 공부(카페)` WHERE 위치=?"
        params = (location,)
        result = get_result_from_9th_db(location)

    else:
        return jsonify({'error': 'Invalid or missing mode parameter'}), 400

    return jsonify({'result': result[0]}) if result else jsonify({'error': 'No results found'}), 404

if __name__ == '__main__':
    app.run(debug=True)