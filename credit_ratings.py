import json

def validate_field(field, value, expected_type, min_val=None, max_val=None, allowed_values=None):
    """
    Validates a single mortgage field based on expected type, range, and allowed values----.
    
    Args:
        field (str): Name of the field being validated.
        value: The actual value provided in the mortgage dictionary.
        expected_type (type or tuple): Expected data type (e.g., int, float, str).
        min_val (int/float, optional): Minimum allowed value (for numerical fields).
        max_val (int/float, optional): Maximum allowed value (for numerical fields).
        allowed_values (list, optional): List of allowed values (for categorical fields).

    Raises:
        TypeError: If the value is not of the expected type.
        ValueError: If the value is out of the allowed range or not in the allowed list.
    """
    if not isinstance(value, expected_type):
        raise TypeError(f"Invalid type for {field}: Expected {expected_type}, got {type(value).__name__}")

    if isinstance(value, (int, float)) and min_val is not None and max_val is not None:
        if not (min_val <= value <= max_val):
            raise ValueError(f"Invalid value for {field}: {value} (Allowed range: {min_val}-{max_val})")

    if allowed_values and value not in allowed_values:
        raise ValueError(f"Invalid value for {field}: {value} (Allowed: {allowed_values})")

def validate_mortgage(mortgage):
    """
    Validates all required fields in a mortgage dictionary.

    Args:
        mortgage (dict): A dictionary containing mortgage details.

    Raises:
        ValueError:  If any required field is missing or has an invalid value.
    """
    required_fields = {
        "credit_score": (int, 300, 850),
        "loan_amount": ((int, float), 0, float("inf")),
        "property_value": ((int, float), 1, float("inf")),
        "annual_income": ((int, float), 1, float("inf")),
        "debt_amount": ((int, float), 0, float("inf")),
        "loan_type": (str, None, None, ["fixed", "adjustable"]),
        "property_type": (str, None, None, ["single_family", "condo"])
    }

    for field, constraints in required_fields.items():
        expected_type = constraints[0]
        min_val, max_val = constraints[1:3]
        allowed_values = constraints[3] if len(constraints) == 4 else None

        if field not in mortgage:
            raise ValueError(f"Missing required field: {field}")

        validate_field(field, mortgage[field], expected_type, min_val, max_val, allowed_values)

def calculate_ltv(mortgage):
    """
    Calculates Loan-to-Value (LTV) ratio.

    Args:
        mortgage (dict): Mortgage dictionary containing loan_amount and property_value.

    Returns:
        float: LTV ratio as a percentage.
    """
    return (mortgage["loan_amount"] / mortgage["property_value"]) * 100

def calculate_dti(mortgage):
    """
    Calculates Debt-to-Income (DTI) ratio.

    Args:
        mortgage (dict): Mortgage dictionary containing debt_amount and annual_income.

    Returns:
        float: DTI ratio as a percentage.
    """
    return (mortgage["debt_amount"] / mortgage["annual_income"]) * 100

def compute_risk_score(mortgage):
    """
    Computes the risk score for a given mortgage based on multiple financial factors.

    Args:
        mortgage (dict): A valid mortgage dictionary.

    Returns:
        tuple: (risk_score, credit_score)
    """
    risk_score = 0

    # Loan-to-Value (LTV) Risk
    ltv = calculate_ltv(mortgage)
    if ltv > 90:
        risk_score += 2
    elif ltv > 80:
        risk_score += 1

    # Debt-to-Income (DTI) Risk
    dti = calculate_dti(mortgage)
    if dti > 50:
        risk_score += 2
    elif dti > 40:
        risk_score += 1

    # Credit Score Contribution
    credit_score = mortgage["credit_score"]
    if credit_score >= 700:
        risk_score -= 1  # Lower risk for high credit score
    elif credit_score < 650:
        risk_score += 1  # Higher risk for low credit score

    # Loan Type Influence
    if mortgage["loan_type"] == "fixed":
        risk_score -= 1  # Lower risk for fixed loans
    elif mortgage["loan_type"] == "adjustable":
        risk_score += 1  # Higher risk for adjustable-rate loans

    # Property Type Influence
    if mortgage["property_type"] == "condo":
        risk_score += 1  # Slightly higher risk for condos

    return risk_score, credit_score

def calculate_credit_rating(mortgages):
    """
    Calculates the overall credit rating for a list of mortgages.

    Args:
        mortgages (list): List of mortgage dictionaries.

    Returns:
        str: The assigned credit rating (AAA, BBB, or C).
    """
    total_risk_score = 0
    total_credit_score = 0
    valid_mortgages = 0

    if not mortgages:
        raise ValueError("The mortgage list cannot be empty.")

    for mortgage in mortgages:
        try:
            validate_mortgage(mortgage)
        except (ValueError, TypeError) as e:
            print(f"Skipping invalid mortgage entry: {e}")
            continue

        risk_score, credit_score = compute_risk_score(mortgage)
        total_risk_score += risk_score
        total_credit_score += credit_score
        valid_mortgages += 1

    if valid_mortgages == 0:
        return "No valid mortgages found."

    # Adjust risk score based on average credit score
    avg_credit_score = total_credit_score / valid_mortgages
    if avg_credit_score >= 700:
        total_risk_score -= 1  # Lower risk for high average credit score
    elif avg_credit_score < 650:
        total_risk_score += 1  # Higher risk for low average credit score

    # Assign Credit Rating based on total risk score
    if total_risk_score <= 2:
        return "AAA"
    elif 3 <= total_risk_score <= 5:
        return "BBB"
    else:
        return "C"

# Example usage
if __name__ == "__main__":
    sample_json = """{
    "mortgages": [
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
    }""" 

    # Load JSON data and compute credit rating
    data = json.loads(sample_json)
    rating = calculate_credit_rating(data["mortgages"])
    print("Credit Rating:", rating)
