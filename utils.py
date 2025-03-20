def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    
    :param height: Height in meters
    :param weight: Weight in kilograms
    :return: BMI value rounded to two decimal places
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    
    :param height: Height in centimeters
    :param weight: Weight in kilograms
    :param age: Age in years
    :param gender: Gender ('male' or 'female')
    :return: BMR value rounded to two decimal places
    """
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender value. Use 'male' or 'female'.")
    
    return round(bmr, 2)
