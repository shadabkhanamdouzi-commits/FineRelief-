"""
Database Migration Setup for FineRelief

This module provides utilities for database versioning and migrations.
Use Alembic for production database version control.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from app.models.models import Base

# Create tables automatically (development)
def init_db():
    """Initialize database with tables"""
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully")

# For production, use Alembic:
# pip install alembic
# alembic init alembic
# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head

if __name__ == "__main__":
    init_db()
