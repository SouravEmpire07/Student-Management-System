"""
Database module.

This module configures the SQLAlchemy engine, local session maker,
and the declarative base class for the SQLite database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Database connection URL (SQLite is used here for local development)
DATABASE_URL = "sqlite:///./student_management.db"

# Create the SQLAlchemy engine.
# connect_args={"check_same_thread": False} is required only for SQLite.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy database models.
    Inherits from DeclarativeBase to enable modern type-annotated models.
    """
    pass


# SessionLocal class. Each instance of SessionLocal will be a database session.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)