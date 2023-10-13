from flask import Flask, jsonify, request

app = Flask(__name__)

# Using a list of dictionaries for users for demonstration purposes
users = [{"username": "exampleUser", "password": "examplePassword"},
         {"username": "exampleUser2", "password": "examplePassword2"}]

@app.route('/login', methods=['POST'])
def login():
    # Extract JSON data from the request
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"userAuthenticated": False, "message": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    # Search for the user in the list of users
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({"userAuthenticated": True}), 200

    return jsonify({"userAuthenticated": False}), 200

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"}), 200

if __name__ == '__main__':
    app.run(debug=False, port=3000)
