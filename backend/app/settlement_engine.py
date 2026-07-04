def calculate_settlement(overdue_months, loan_type):
    if overdue_months >= 12:
        percentage = 60
        priority = "High"
    elif overdue_months >= 6:
        percentage = 45
        priority = "Medium"
    else:
        percentage = 30
        priority = "Low"

    if loan_type.lower() == "personal":
        percentage += 5

    return {
        "settlement_percentage": percentage,
        "priority": priority
    }
def generate_negotiation_letter(lender_name, settlement_percentage):
    return f"""
Dear {lender_name},

I am currently facing financial difficulties and request your consideration for a settlement.

I kindly request a settlement of approximately {settlement_percentage}% of the outstanding loan amount.

Thank you for your understanding.

Sincerely,
Customer
"""