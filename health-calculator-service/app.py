from flask import Flask, request, jsonify
from health_test import calculate_bmi, calculate_bmr

app = Flask(__name__)
 
@app.route('/bmi', methods=['GET'])
def bmi():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    if not height or not weight:
        return jsonify({"error": "Les paramètres 'height' et 'weight' sont requis"}), 400
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"bmi": bmi_value})
    
    
 
@app.route('/bmr', methods=['POST'])
def bmr():
   
    data = request.get_json()
 
    
    height = data.get('height')  
    weight = data.get('weight') 
    age = data.get('age')        
    gender = data.get('gender')  
 
    
    if not height or not weight or not age or not gender:
        return jsonify({"error": "Les paramètres 'height', 'weight', 'age', et 'gender' sont requis"}), 400
 
    
    bmr_value = calculate_bmr(height, weight, age, gender)
   

    return f"<h1>Votre TMB est {bmr_value:.2f} calories par jour</h1>"
  
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 