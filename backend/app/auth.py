from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import SessionLocal
from app.models.models import User
from app.auth_utils import verify_password, create_token
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        # OAuth2PasswordRequestForm uses "username" field as email
        email = (form_data.username or "").strip().lower()
        password = form_data.password or ""

        user = db.query(User).filter(User.email == email).first()

        if not user:
            logger.warning("Login failed: user not found for email=%s", email)
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if not verify_password(password, user.password):
            logger.warning("Login failed: password mismatch for email=%s", email)
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_token({"sub": user.email})

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.exception("Login failed with server error")
        raise HTTPException(status_code=500, detail=f"Login failed: {str(e)}")