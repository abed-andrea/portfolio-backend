#for reading environment variables
import os

#the thing that actually conencts sqlalchemy to the database
from sqlalchemy import create_engine

#session = temporary convo with db to query
#DeclarativeBase = the "parent class" your SQLAlchemy models inherit from (aka the template that tells SQLAlchemy "these classes are database tables")
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# 1) Build the database URL.
# In docker-compose, the DB host is the service name: "db"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://portfolio_user:portfolio_password@db:5432/portfolio_db" #fallback
)


# 2) The Engine knows how to connect to the DB.
engine = create_engine(DATABASE_URL, echo=True)


# 3) SessionLocal is what we use to open/close DB sessions per request.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# 4) Base is what our models inherit from.
class Base(DeclarativeBase):
    pass