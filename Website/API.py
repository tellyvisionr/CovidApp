from flask import Blueprint, jsonify, request, redirect

API = Blueprint('API', __name__)

@API.route('/api/test', methods=['GET'])
def test():
    return jsonify(message="Hello from API"), 200
# For demonstration purposes, using hardcoded username and password
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

@API.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get("username") == VALID_USERNAME and data.get("password") == VALID_PASSWORD:
        return jsonify(userAuthenticated="true"), 200
        


if __name__ == '__main__':
    app.run(debug=True)
