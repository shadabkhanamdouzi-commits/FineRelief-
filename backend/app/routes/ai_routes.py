from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import (
    NegotiationRequest,
    ProfileUpdate,
    LoanCreate
)

from app.database import SessionLocal
from app.ai_negotiation_engine import generate_negotiation_strategy
from app.settlement_engine import calculate_settlement

router = APIRouter()


# ========================
# AI NEGOTIATION STRATEGY
# ========================
@router.post("/ai-negotiation-strategy")
def ai_negotiation_strategy(request: NegotiationRequest):
    strategy = generate_negotiation_strategy(request)

    return {
        "strategy": strategy
    }


# ========================
# LOAN SETTLEMENT
# ========================
@router.post("/loan-settlement")
def loan_settlement(request: NegotiationRequest):
    result = calculate_settlement(
        request.overdue_months,
        "personal"
    )

    # FIX: no generate_negotiation_letter needed
    letter = (
        f"Dear {request.lender_name}, "
        f"we would like to propose a settlement of "
        f"{result['settlement_percentage']}% due to overdue status. "
        f"Please consider this offer for closure of the loan account."
    )

    return {
        "settlement_percentage": result["settlement_percentage"],
        "priority": result["priority"],
        "letter": letter
    }


# ========================
# DB SESSION
# ========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ========================
# UPDATE PROFILE
# ========================
@router.put("/update-profile")
def update_profile(profile: ProfileUpdate):
    return {
        "message": "Profile Updated Successfully",
        "monthly_income": profile.monthly_income,
        "monthly_expenses": profile.monthly_expenses,
        "lump_sum_available": profile.lump_sum_available
    }


# ========================
# ADD LOAN
# ========================
@router.post("/add-loan")
def add_loan(loan: LoanCreate):
    return {
        "message": "Loan Added Successfully",
        "loan": {
            "lender_name": loan.lender_name,
            "outstanding_amount": loan.outstanding_amount,
            "interest_rate": loan.interest_rate,
            "emi": loan.emi,
            "overdue_months": loan.overdue_months,
            "loan_type": loan.loan_type
        }
    }