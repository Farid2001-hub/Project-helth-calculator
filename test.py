import unittest
from utils import calculate_bmi, calculate_bmr

class TestHealthCalculatorUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        # Test avec un cas de BMI normal
        height = 1.75  # taille en mètres
        weight = 70    # poids en kilogrammes
        expected_bmi = 22.86  # résultat attendu
        result = calculate_bmi(height, weight)
        self.assertAlmostEqual(result, expected_bmi, places=2)

    def test_calculate_bmi_underweight(self):
        # Test pour un cas de sous-poids
        height = 1.80  # taille en mètres
        weight = 50    # poids en kilogrammes
        expected_bmi = 15.43  # résultat attendu
        result = calculate_bmi(height, weight)
        self.assertAlmostEqual(result, expected_bmi, places=2)

    def test_calculate_bmr_male(self):
        # Test pour un homme
        height = 175  # taille en cm
        weight = 70   # poids en kg
        age = 25      # âge en années
        gender = 'male'
        expected_bmr = 1724.05  # résultat attendu ajusté
        result = calculate_bmr(height, weight, age, gender)
        self.assertAlmostEqual(result, expected_bmr, places=2)

    def test_calculate_bmr_female(self):
        # Test pour une femme
        height = 160  # taille en cm
        weight = 60   # poids en kg
        age = 30      # âge en années
        gender = 'female'
        expected_bmr = 1368.19  # résultat attendu ajusté
        result = calculate_bmr(height, weight, age, gender)
        self.assertAlmostEqual(result, expected_bmr, places=2)

    def test_calculate_bmr_invalid_gender(self):
        # Test pour un genre invalide
        height = 175  # taille en cm
        weight = 70   # poids en kg
        age = 25      # âge en années
        gender = 'other'
        with self.assertRaises(ValueError):
            calculate_bmr(height, weight, age, gender)

if __name__ == '__main__':
    unittest.main()
