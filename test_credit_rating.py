import unittest
from credit_ratings import calculate_credit_rating

class TestCreditRating(unittest.TestCase):
    
    def test_high_credit_score_low_risk(self):
        mortgages = [
            {
                "credit_score": 800,
                "loan_amount": 100000,
                "property_value": 200000,
                "annual_income": 80000,
                "debt_amount": 10000,
                "loan_type": "fixed",
                "property_type": "single_family"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")

    def test_medium_risk(self):
        mortgages = [
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "BBB")

    def test_high_risk(self):
        mortgages = [
            {
                "credit_score": 600,
                "loan_amount": 250000,
                "property_value": 260000,
                "annual_income": 40000,
                "debt_amount": 30000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "C")

    def test_average_credit_score_adjustment(self):
        mortgages = [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(calculate_credit_rating(mortgages), "AAA")


if __name__ == "__main__":
    unittest.main()
