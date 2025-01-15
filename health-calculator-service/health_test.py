def calculate_bmi(height, weight):
    """Calcule l'IMC en fonction de la taille et du poids"""
    return weight / (height ** 2)
 
def calculate_bmr(height, weight, age, gender):
    """Calcule le TMB en utilisant l'équation de Harris-Benedict."""
    if gender == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
 