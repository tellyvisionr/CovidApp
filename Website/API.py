from flask import Blueprint, jsonify, request, redirect
import pickle
import os
API = Blueprint('API', __name__)

current_directory = os.path.dirname(os.path.abspath(__file__))
assets_directory = os.path.join(current_directory, 'Assets/Model')
imputer_file_path = os.path.join(assets_directory, 'imputer.pkl')
model_file_path = os.path.join(assets_directory, 'model.pkl')

with open(model_file_path, "rb") as model_file:
    model = pickle.load(model_file)

with open(imputer_file_path, "rb") as imputer_file:
    imputer = pickle.load(imputer_file)


def reformat_input(content):
    feature_map = {
        'SEX': {'male': 0, 'female': 1},
        'DIABETES': {'yes': 1, 'no': 0},
        'OBESITY': {'yes': 1, 'no': 0},
        'ASTHMA': {'yes': 1, 'no': 0},
        'TOBACCO': {'yes': 1, 'no': 0},
        'PATIENT_TYPE': {'yes': 1, 'no': 0}
    }
    
    reformatted_content = {}
    for feature, mapping in feature_map.items():
        value = content.get(feature, '').lower()
        reformatted_content[feature] = mapping.get(value, None)
        
    reformatted_content['AGE'] = int(content.get('AGE', 0))

    return reformatted_content


@API.route("/api/predict", methods=["POST"])
def predict():
    try:
        #example input {"SEX": "male", "AGE": 20, "DIABETES": "yes", "OBESITY": "yes", "ASTHMA": "yes", "TOBACCO": "yes", "PATIENT_TYPE": "no"}
        # Parse input features from JSON
        content = request.json
        reformatted_content = reformat_input(content)
        
        feature_array = [
            reformatted_content['SEX'],
            reformatted_content['AGE'],
            reformatted_content['DIABETES'],
            reformatted_content['OBESITY'],
            reformatted_content['ASTHMA'],
            reformatted_content['TOBACCO'],
            reformatted_content['PATIENT_TYPE']
        ]
        # Handle missing values using the imputer
        feature_array = imputer.transform([feature_array])

        # Make prediction
        prediction = model.predict_proba(feature_array)
        
        # Return probability (the second class)
        return jsonify({"probability": prediction[0][1]})

    except Exception as e:
        return jsonify({"error": str(e)})



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
