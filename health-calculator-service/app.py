from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

# Initialisation de l'application Flask
app = Flask(__name__)

# Route pour le calcul de l'IMC (Indice de Masse Corporelle)
@app.route('/bmi', methods=['GET'])
def bmi():
    # Récupération des données JSON envoyées par la requête
    data = request.get_json()

    # Extraction de la taille et du poids à partir des données JSON
    height = data.get('height')
    weight = data.get('weight')

    # Vérification de la présence des paramètres 'height' et 'weight'
    if not height or not weight:
        # Retour d'une erreur si les paramètres sont manquants
        return jsonify({"error": "Les paramètres 'height' et 'weight' sont requis"}), 400

    # Calcul de l'IMC en utilisant la fonction calculate_bmi
    bmi_value = calculate_bmi(height, weight)

    # Retour d'un JSON contenant la valeur de l'IMC
    return jsonify({"bmi": bmi_value})

# Route pour le calcul du TMB (Taux Métabolique Basal)
@app.route('/bmr', methods=['POST'])
def bmr():
    # Récupération des données JSON envoyées par la requête
    data = request.get_json()

    # Extraction de la taille, du poids, de l'âge et du sexe à partir des données JSON
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')

    # Vérification de la présence de tous les paramètres requis
    if not height or not weight or not age or not gender:
        # Retour d'une erreur si des paramètres sont manquants
        return jsonify({"error": "Les paramètres 'height', 'weight', 'age', et 'gender' sont requis"}), 400

    # Calcul du TMB en utilisant la fonction calculate_bmr
    bmr_value = calculate_bmr(height, weight, age, gender)

    # Création d'une chaîne HTML avec la valeur du TMB
    return f"<h1>Votre TMB est {bmr_value:.2f} calories par jour</h1>"

# Point d'entrée de l'application
if __name__ == '__main__':
    # Démarrage de l'application sur le port 5000 et accessible depuis n'importe quelle adresse IP
    app.run(host='0.0.0.0', port=5000)