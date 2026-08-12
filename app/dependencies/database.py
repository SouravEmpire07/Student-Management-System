from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Database dependency provider for FastAPI routes.
    
    Creates a new SQLAlchemy session for each request, yields it, and
    ensures it is closed once the request lifecycle is complete.
    
    Yields:
        Generator[Session, None, None]: The database session.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        # Guarantee database connection closure after the response is sent.
        db.close()