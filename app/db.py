import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://portfolio_user:portfolio_password@db:5432/portfolio_db" #fallback
)


engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True,
    pool_recycle=300,
    echo=True)


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


# FastAPI dependency: provides a DB session per request
def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()